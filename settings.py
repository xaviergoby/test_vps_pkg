import os

# OS Dir Paths
## General
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # returns C:\Users\XGOBY\OneDrive\HODL\HODL_Research_Analysis
DATA_DIR = os.path.join(ROOT_DIR, "data")  # C:\Users\XGOBY\OneDrive\HODL\HODL_Research_Analysis\data_sources

# Logs & all else
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

## Bittensor
BITTENSOR_DATA_DIR = os.path.join(DATA_DIR, "bittensor")  # C:\Users\XGOBY\OneDrive\HODL\HODL_Research_Analysis\data_sources\bittensor

BITTENSOR_OTC_EX_DATA_DIR = os.path.join(BITTENSOR_DATA_DIR, "otc_exchange_data")  # C:\Users\XGOBY\OneDrive\HODL\HODL_Research_Analysis\data_sources\bittensor\otc_exchange_data
TEST_BITTENSOR_OTC_EX_DATA_DIR = os.path.join(BITTENSOR_DATA_DIR, "test_otc_exchange_data")  # C:\Users\XGOBY\OneDrive\HODL\HODL_Research_Analysis\data_sources\bittensor\otc_exchange_data

CMPLT_ORDERS_DATASET_DIR = os.path.join(BITTENSOR_OTC_EX_DATA_DIR, "cmplt_orders_dataset")
TEST_CMPLT_ORDERS_DATASET_DIR = os.path.join(TEST_BITTENSOR_OTC_EX_DATA_DIR, "cmplt_orders_dataset")

BITTENSOR_LOGS_TXT_FILE = os.path.join(LOGS_DIR, "bittensor_otc_exchange_data_download_logs.txt")
TEST_BITTENSOR_LOGS_TXT_FILE = os.path.join(LOGS_DIR, "test_bittensor_otc_exchange_data_download_logs.txt")


SCRAPED_DATASETS_DIR = os.path.join(BITTENSOR_DATA_DIR, "scraped_datasets")