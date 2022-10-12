import numpy as np
from test_pkg_module import test_pkg_module_script
from test_pkg_module import bittensor_otc_ex_data_miner
import time
def print_numpy_pkg_version():
    np_pkg_ver = np.__version__
    np_pkg_ver_info_str = f"Numpy version: {np_pkg_ver}"
    return np_pkg_ver_info_str





if __name__ == "__main__":
    print(print_numpy_pkg_version())
    print(test_pkg_module_script.print_python_ver())
    print(test_pkg_module_script.msg_for_bbz())
    otc_ex_data_scraper = bittensor_otc_ex_data_miner.OTCExchangeDataScraper()
    print("Downloading bittensor OTC exchange data as csv")
    otc_ex_data_scraper.save_otc_ex_order_book_csv_data("1")
    print("Sleeping for 3 seconds...")
    time.sleep(3)
    print("Downloading bittensor OTC exchange data as csv")
    otc_ex_data_scraper.save_otc_ex_order_book_csv_data("2")

