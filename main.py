from test_pkg_module import bittensor_otc_ex_data_miner
import time


def main(test_mode=False, verbosity=1):
    otc_ex_data_scraper = bittensor_otc_ex_data_miner.OTCExchangeDataScraper()
    # otc_ex_data_scraper.dl_otc_ex_tick_order_book_dataset()
    otc_ex_data_scraper.run(test_mode=test_mode, verbosity=verbosity)



if __name__ == "__main__":
    main()

