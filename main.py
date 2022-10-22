from test_pkg_module import bittensor_otc_ex_data_miner
import time
import psutil

def main(dl_mode="batch", test_mode=False, verbosity=1):
    otc_ex_data_scraper = bittensor_otc_ex_data_miner.OTCExchangeDataScraper()
    # otc_ex_data_scraper.dl_otc_ex_tick_order_book_dataset()
    otc_ex_data_scraper.run(dl_mode, test_mode, verbosity)

def main_event_loop(dl_delay_mins=5, dl_events_cnt=None, dl_mode="batch", test_mode=False, verbosity=1):
    otc_ex_data_scraper = bittensor_otc_ex_data_miner.OTCExchangeDataScraper()
    if dl_events_cnt is None:
        print(f"Downloading data every {dl_delay_mins} minuets for INFINITE minuets")
        dl_nonstop_cnt = 0
        while True:
            dl_nonstop_cnt = dl_nonstop_cnt + 1
            if verbosity == 1:
                print(f"Downloading data in {dl_mode} mode | Batch #: {dl_nonstop_cnt}")
            otc_ex_data_scraper.run(dl_mode, test_mode, verbosity)
            if verbosity == 1:
                print(f"Sleeping for {dl_delay_mins} minuets")
            time.sleep(dl_delay_mins * 60)
    elif dl_events_cnt is not None:
        print(f"Downloading data every {dl_delay_mins} minuets for {dl_delay_mins*dl_events_cnt} minuets")
        for dl_event_cnt_i in range(dl_events_cnt):
            if verbosity == 1:
                print(f"Downloading data in {dl_mode} mode | Batch #: {dl_event_cnt_i+1}")
            otc_ex_data_scraper.run(dl_mode, test_mode, verbosity)
            if verbosity == 1:
                print(f"Sleeping for {dl_delay_mins} minuets")
                time.sleep(dl_delay_mins * 60)





if __name__ == "__main__":
    # main()
    main_event_loop(dl_delay_mins=1, dl_events_cnt=5, dl_mode="batch", test_mode=False, verbosity=1)
    # main_event_loop(dl_delay_mins=5, dl_events_cnt=3, dl_mode="batch", test_mode=False, verbosity=1)

