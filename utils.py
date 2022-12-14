# https://tonyteaches.tech/digitalocean-api-python/

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



if __name__ == "__main__":
    # 15-10-2022_07-43_sell_orders.csv
    # 15-10-2022_07-44_buy_orders.csv
    # 15-10-2022_07-43_sell_orders.csv
    # 15-10-2022_07-44_buy_orders.csv
    import settings
    # txt_file_path = settings.BITTENSOR_LOGS_TXT_FILE
    txt_file_path = settings.TEST_BITTENSOR_LOGS_TXT_FILE
