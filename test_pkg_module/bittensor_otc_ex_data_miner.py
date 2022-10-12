import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
# import settings
import os

class OTCExchangeDataScraper:

    def __init__(self):
        self.url = "https://bittensor.exchange/"
        # self.__sell_orders_dict = {"Prices", "Volume", "Total"}
        self.__order_book_bs4_table_content = None
        self.__sell_orders_dict = None
        self.__sell_orders_df = None
        self.__buy_orders_dict = None

    @property
    def current_dt_str(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M")

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
        current_dt_str = self.current_dt_str
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

    def save_otc_ex_order_book_csv_data(self):
        sell_orders_df, buy_orders_df = self.build_order_book_dfs()
        # sell_orders_csv_file_name = sell_orders_df["Datetime"][0].replace("/", "-").replace(" ", "_").replace(":", "-")
        # sell_orders_csv_file_path = os.path.join(settings.BITTENSOR_OTC_EX_DATA_DIR, f"sell_orders/{sell_orders_csv_file_name}_sell_orders.csv")
        # buy_orders_csv_file_name = buy_orders_df["Datetime"][0].replace("/", "-").replace(" ", "_").replace(":", "-")
        # buy_orders_csv_file_path = os.path.join(settings.BITTENSOR_OTC_EX_DATA_DIR, f"buy_orders/{buy_orders_csv_file_name}_buy_orders.csv")
        sell_orders_df.to_csv("sell_orders.csv")
        buy_orders_df.to_csv("buy_orders.csv")




if __name__ == "__main__":
    otc_ex_data_scraper = OTCExchangeDataScraper()
    # sell_orders_df, buy_orders_df = otc_ex_data_scraper.build_order_book_dfs()
    # print(f"sell_orders_df:\n{sell_orders_df}")
    # print(f"buy_orders_df:\n{buy_orders_df}")
    otc_ex_data_scraper.save_otc_ex_order_book_csv_data()