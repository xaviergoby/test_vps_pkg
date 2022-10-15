from datetime import datetime


def read_txt_file(txt_file_path):
    with open(txt_file_path, "r") as file_obj:
        contents = [line.strip() for line in file_obj.readlines()]
        file_obj.close()
        return contents


def update_orders_download_logs(log_file_path, log_msg):
    with open(log_file_path, "a") as file_obj:
        log_msg_formatted = f"{log_msg}\n"
        file_obj.write(log_msg_formatted)
        file_obj.close()

    # logs = read_txt_file(log_file_path)
    # updated_logs = logs.append(log_msg)

# destFile = r"C:\Test\Test.txt"
# with open(destFile, 'a') as f:
#     f.write("some appended text")



if __name__ == "__main__":
    # 15-10-2022_07-43_sell_orders.csv
    # 15-10-2022_07-44_buy_orders.csv
    # 15-10-2022_07-43_sell_orders.csv
    # 15-10-2022_07-44_buy_orders.csv
    import settings
    # txt_file_path = settings.BITTENSOR_LOGS_TXT_FILE
    txt_file_path = settings.BITTENSOR_TEST_LOGS_TXT_FILE

    res1  = read_txt_file(txt_file_path)
    # 15/10/2022 07:43 | BUY 28 | SELL 54 | TOTAL 82

    update_orders_download_logs(txt_file_path, "15/10/2022 07:45 | BUY 28 | SELL 54 | TOTAL 82")
    update_orders_download_logs(txt_file_path, "15/10/2022 07:46 | BUY 29 | SELL 52 | TOTAL 81")
    update_orders_download_logs(txt_file_path, "15/10/2022 07:47 | BUY 25 | SELL 59 | TOTAL 84")

    res2 = read_txt_file(txt_file_path)



# bittensor_otc_exchange_data_download_logs.txt