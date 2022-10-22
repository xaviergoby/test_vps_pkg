import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
import settings
import utils
import os
from typing import Iterator, Tuple

class OTCExchangeDataScraper:

    def __init__(self):
        self.url = "https://bittensor.exchange/"
        # self.__sell_orders_dict = {"Prices", "Volume", "Total"}
        self.__order_book_bs4_table_content = None
        self.__sell_orders_dict = None
        self.__sell_orders_df = None
        self.__buy_orders_dict = None
        self.__current_tick_dt = None
        self.__current_tick_order_book = None
        self.__current_tick_sell_orders_dl_cnt = None
        self.__current_tick_buy_orders_dl_cnt = None

    # ############################## Current Property Cls Instance Attr Accessor Methods

    @property
    def current_dt(self):
        return datetime.now()

    @property
    # def current_tick_order_book(self) -> tuple[pd.DataFrame]:
    def current_tick_order_book(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        :return: i.e. sell_orders_df, buy_orders_df
        """
        return self.__current_tick_order_book

    @property
    def current_tick_sell_orders_dl_cnt(self):
        return self.__current_tick_sell_orders_dl_cnt
    @property
    def current_tick_buy_orders_dl_cnt(self):
        return self.__current_tick_buy_orders_dl_cnt

    def current_dt_str(self, dt_str_format=None):
        if dt_str_format is None:
            return self.__current_tick_dt.strftime("%d/%m/%Y %H:%M")
        else:
            return self.__current_tick_dt.strftime(dt_str_format)

    # ############################## Methods Of Required Functionalities

    def get_page_request_response_content(self):
        response = requests.get(self.url)
        content = response.content
        return content

    def get_n_parse_table_content(self):
        content = self.get_page_request_response_content()
        soup = BeautifulSoup(content, "html.parser")
        table_content = soup.find_all('table', attrs={'class': 'table table-striped'})
        return table_content

    def build_sell_orders_dict(self, sell_orders_table_content):
        sell_orders = sell_orders_table_content.find_all('td', attrs={'class': 'text-nowrap'})
        sell_order_vols = [float(sell_order_vol_i.text.strip().replace("τ ", "").replace(".00", "").replace(",", ""))
                           for sell_order_vol_i in sell_orders[::2]]
        sell_order_totals = [float(i.text.strip().replace("$ ", "").replace(",", "")) for i in sell_orders[1::2]]
        sell_order_prices = np.round((np.array(sell_order_totals) / np.array(sell_order_vols)).tolist(), 2)
        sell_orders_dict = {"Prices": sell_order_prices, "Volume": sell_order_vols, "Total": sell_order_totals}
        return sell_orders_dict

    def build_buy_orders_dict(self, buy_orders_table_content):
        buy_orders = buy_orders_table_content.find_all('td', attrs={'class': 'text-nowrap'})
        buy_order_vols = [float(buy_order_vol_i.text.strip().replace("τ ", "").replace(".00", "").replace(",", "")) for
                          buy_order_vol_i in buy_orders[::2]]
        buy_order_totals = [float(i.text.strip().replace("$ ", "").replace(",", "")) for i in buy_orders[1::2]]
        buy_order_prices = np.round((np.array(buy_order_totals) / np.array(buy_order_vols)).tolist(), 2)
        buy_orders_dict = {"Prices": buy_order_prices, "Volume": buy_order_vols, "Total": buy_order_totals}
        return buy_orders_dict

    def build_order_book_dicts(self, table_content=None):
        current_dt_str = self.current_dt_str()
        # __create_tick_order_book_file_paths
        # current_dt_str = self.current_dt.strftime()
        if table_content is None:
            sell_orders_table_content, buy_orders_table_content = self.get_n_parse_table_content()
        else:
            sell_orders_table_content, buy_orders_table_content = table_content
        # sell_orders_table_content, buy_orders_table_content = self.order_book_bs4_table_content
        sell_orders_dict = self.build_sell_orders_dict(sell_orders_table_content)
        buy_orders_dict = self.build_buy_orders_dict(buy_orders_table_content)
        sell_orders_dt_str_col_list = [current_dt_str] * len(sell_orders_dict["Prices"])
        sell_orders_dict["Datetime"] = sell_orders_dt_str_col_list
        buy_orders_dt_str_col_list = [current_dt_str] * len(buy_orders_dict["Prices"])
        buy_orders_dict["Datetime"] = buy_orders_dt_str_col_list
        return sell_orders_dict, buy_orders_dict

    def build_order_book_dfs(self):
        sell_orders_dict, buy_orders_dict = self.build_order_book_dicts()
        sell_orders_df = pd.DataFrame.from_dict(sell_orders_dict)
        sell_orders_df = sell_orders_df.reindex(columns=["Datetime", "Prices", "Volume", "Total"])
        buy_orders_df = pd.DataFrame.from_dict(buy_orders_dict)
        buy_orders_df = buy_orders_df.reindex(columns=["Datetime", "Prices", "Volume", "Total"])
        return sell_orders_df, buy_orders_df

    def create_updated_cmplt_orders_dfs(self, current_sell_orders, current_buy_orders):
        if len(os.listdir(settings.CMPLT_ORDERS_DATASET_DIR)) == 0:
            return current_sell_orders, current_buy_orders
        else:
            past_sell_orders = pd.read_csv(os.path.join(settings.CMPLT_ORDERS_DATASET_DIR, "sell_orders.csv"))
            past_buy_orders = pd.read_csv(os.path.join(settings.CMPLT_ORDERS_DATASET_DIR, "buy_orders.csv"))
            updated_cmplt_sell_orders_dataset_df = pd.concat([past_sell_orders, current_sell_orders])
            updated_cmplt_buy_orders_dataset_df = pd.concat([past_buy_orders, current_buy_orders])
            return updated_cmplt_sell_orders_dataset_df, updated_cmplt_buy_orders_dataset_df

    # ############################## Downloaded datasets save abs save path locations

    def create_tick_order_book_abs_dl_file_paths(self, test_mode=False):
        """
        :param test_mode: By default test_mode=False and therefore the
        sell & buy orders csv files are saved to the location @ path:
        data/bittensor/otc_exchange_data/ If test_mode=True, the sell
        & buy orders csv files are saved to the location @ path:
        data/bittensor/test_otc_exchange_data/
        :return: a 2-tuple of strings, i.e.:
        (tick_ob_sell_orders_abs_path, tick_ob_buy_orders_abs_path)
        """
        current_tick_dt_file_format_str = self.current_dt_str("%d-%m-%Y_%H-%M")
        # Create the file names for the buy & sell orders csv files
        current_tick_ob_sell_orders_file_name = f"{current_tick_dt_file_format_str}_sell_orders.csv"
        current_tick_ob_buy_orders_file_name = f"{current_tick_dt_file_format_str}_buy_orders.csv"
        # Create the relative paths to the buy & sell orders csv files
        current_tick_ob_sell_orders_file_rel_path = f"sell_orders/{current_tick_ob_sell_orders_file_name}"
        current_tick_ob_buy_orders_file_rel_path = f"buy_orders/{current_tick_ob_buy_orders_file_name}"
        # Create the absolute paths to the buy & sell orders csv files
        # First check to see whether data is being downloaded in "test_mode" or not.
        if test_mode is True:
            sell_orders_csv_file_abs_path = os.path.join(settings.TEST_BITTENSOR_OTC_EX_DATA_DIR,
                                                         current_tick_ob_sell_orders_file_rel_path)
            buy_orders_csv_file_abs_path = os.path.join(settings.TEST_BITTENSOR_OTC_EX_DATA_DIR,
                                                        current_tick_ob_buy_orders_file_rel_path)
        else:
            sell_orders_csv_file_abs_path = os.path.join(settings.BITTENSOR_OTC_EX_DATA_DIR,
                                                         current_tick_ob_sell_orders_file_rel_path)
            buy_orders_csv_file_abs_path = os.path.join(settings.BITTENSOR_OTC_EX_DATA_DIR,
                                                        current_tick_ob_buy_orders_file_rel_path)

        return sell_orders_csv_file_abs_path, buy_orders_csv_file_abs_path

    def create_cmplt_order_book_dataset_abs_dl_file_paths(self, test_mode=False):
        """
        :param test_mode: # By default test_mode=False and therefore the
        sell & buy orders csv files are saved to the location @ path:
        data/bittensor/otc_exchange_data/ If test_mode=True, the sell
        & buy orders csv files are saved to the location @ path:
        data/bittensor/test_otc_exchange_data/
        :return: a 2-tuple of strings, i.e.:
        (tick_ob_sell_orders_abs_path, tick_ob_buy_orders_abs_path)
        """
        # current_tick_dt_file_format_str = self.current_dt_str("%d-%m-%Y_%H-%M")
        if test_mode is True:
            cmplt_OB_sell_orders_abs_df_file_path = os.path.join(settings.TEST_CMPLT_ORDERS_DATASET_DIR,
                                                                 "sell_orders.csv")
            cmplt_OB_buy_orders_abs_df_file_path = os.path.join(settings.TEST_CMPLT_ORDERS_DATASET_DIR,
                                                                "buy_orders.csv")
            return cmplt_OB_sell_orders_abs_df_file_path, cmplt_OB_buy_orders_abs_df_file_path
        else:
            cmplt_OB_sell_orders_abs_df_file_path = os.path.join(settings.CMPLT_ORDERS_DATASET_DIR,
                                                                 "sell_orders.csv")
            cmplt_OB_buy_orders_abs_df_file_path = os.path.join(settings.CMPLT_ORDERS_DATASET_DIR,
                                                                "buy_orders.csv")

        return cmplt_OB_sell_orders_abs_df_file_path, cmplt_OB_buy_orders_abs_df_file_path

    # ############################## Main Functional Processes Methods ##############################
    # ############### Driving Update Methods ###############
    def update_current_tick_dt(self):
        """
        STEP 1
        :return: None
        """
        self.__current_tick_dt = self.current_dt

    def update_current_tick_order_book(self):
        """
        STEP 2
        :return: None
        """
        self.__current_tick_order_book = self.build_order_book_dfs()

    def update_current_tick_OB_sell_n_buy_orders_dl_cnt(self):
        """
        STEP 3
        :return: None
        """
        sell_n_buy_orders_dl_cnt = tuple(map(lambda OB_side: OB_side.shape[0], self.current_tick_order_book))
        self.__current_tick_sell_orders_dl_cnt, self.__current_tick_buy_orders_dl_cnt = sell_n_buy_orders_dl_cnt

    def dl_create_n_save_current_ex_OB_datasets(self, dl_mode, test_mode=False):
        """
        STEP 4
        :param test_mode: By default test_mode=False and therefore the
        sell & buy orders csv files are saved to the location @ path:
        data/bittensor/otc_exchange_data/ If test_mode=True, the sell
        & buy orders csv files are saved to the location @ path:
        data/bittensor/test_otc_exchange_data/
        :return:
        """
        # Get the sell orders & buy orders of the current tick exchange order book
        # CURRENT OTC ex TICK order book datasets
        sell_orders_df, buy_orders_df = self.current_tick_order_book
        self.__current_tick_sell_orders_dl_cnt = sell_orders_df.shape[0]
        self.__current_tick_buy_orders_dl_cnt = buy_orders_df.shape[0]
        # CURRENT OTC ex TICK order book dataset file paths
        sell_orders_csv_file_abs_path, buy_orders_csv_file_abs_path = self.create_tick_order_book_abs_dl_file_paths(test_mode)
        # Save CURRENT OTC ex TICK order book datasets
        if dl_mode == "batch":
            sell_orders_df.to_csv(sell_orders_csv_file_abs_path)
            buy_orders_df.to_csv(buy_orders_csv_file_abs_path)
        if dl_mode == "cmplt" or dl_mode == "complete" or dl_mode == "all":
            # CMPLT OTC ex order book datasets
            updated_cmplt_OB_dataset_dfs = self.create_updated_cmplt_orders_dfs(sell_orders_df, buy_orders_df)
            updated_cmplt_sell_orders_dataset_df, updated_cmplt_buy_orders_dataset_df = updated_cmplt_OB_dataset_dfs
            # CMPLT OTC ex order book dataset file paths
            cmplt_OB_abs_csv_file_paths = self.create_cmplt_order_book_dataset_abs_dl_file_paths(test_mode)
            cmplt_OB_sell_orders_abs_csv_file_path, cmplt_OB_buy_orders_abs_csv_file_path = cmplt_OB_abs_csv_file_paths
            # Save CMPLT OTC ex order book datasets
            updated_cmplt_sell_orders_dataset_df.to_csv(cmplt_OB_sell_orders_abs_csv_file_path)
            updated_cmplt_buy_orders_dataset_df.to_csv(cmplt_OB_buy_orders_abs_csv_file_path)


    # ############################## Main Run Method ##############################

    def run_otc_ex_tick(self, dl_mode="batch", test_mode=False, verbosity=1):
        """
        :param test_mode: If True then data is NOT saved to bittensor/otc_exchange_data dir! Instead,
        if deny_save is left as the def False then data is saved to the bittensor/test_otc_exchange_data dir
        BUT if deny_save is True then data is not saved at all & is instead returned by the function as a 2-tuple
        of dataframes consisting of sell orders & buy orders
        instead of bittensor/otc_exchange_data dir.
        :return:
        """
        # STEP 1
        # Set the current datetime.now() datetimee instance  of
        # the `self.__current_tick_dt` cls instance attr variable
        self.update_current_tick_dt()
        # STEP 2
        # Build the order book of the OTC exchange at the current
        # self.__current_tick_dt <%d/%m/%Y %H:%M> date & time & set
        # it as the val of the cls instance attr var
        # self.__current_tick_order_book.
        self.update_current_tick_order_book()
        # STEP 3
        self.update_current_tick_OB_sell_n_buy_orders_dl_cnt()
        # STEP 4
        self.dl_create_n_save_current_ex_OB_datasets(dl_mode, test_mode)

        msg = f"{self.current_dt_str()} | " \
              f"BUY {self.current_tick_buy_orders_dl_cnt} | " \
              f"SELL {self.current_tick_sell_orders_dl_cnt} | " \
              f"TOTAL {self.current_tick_buy_orders_dl_cnt+self.current_tick_sell_orders_dl_cnt}"

        # MISC STEP
        utils.update_orders_download_logs(settings.BITTENSOR_LOGS_TXT_FILE, msg)

        if verbosity == 1:
            print(msg)

    def run(self, dl_mode="batch", test_mode=False, verbosity=1):
        self.run_otc_ex_tick()




if __name__ == "__main__":
    otc_ex_data_scraper = OTCExchangeDataScraper()
    # otc_ex_data_scraper.dl_otc_ex_tick_order_book_dataset()
    # otc_ex_data_scraper.run_otc_ex_tick(test_mode=False)
    otc_ex_data_scraper.run(dl_mode="batch", test_mode=False, verbosity=1)

