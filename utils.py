# https://tonyteaches.tech/digitalocean-api-python/
# import digitalocean
import os
import time
import glob
import requests
from datetime import datetime


# def request_remote_VM_Droplet_server():
#     # second_DO_Droplet_token
#     # dop_v1_9cfd75e687455030b9d694461ceef0f33fb3fcc25f3aa29d8ebdf9467b807489
#
#
#     # api_key = "dop_v1_67669282824d53fb09bd774b65f15d384919361b621e55d9dbd70ceb03cad235"
#     token = "dop_v1_9cfd75e687455030b9d694461ceef0f33fb3fcc25f3aa29d8ebdf9467b807489"
#     api_key_name = "first_DO_token"
#     headers = {
#         # Already added when you pass json= but not when you pass data=
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {token}',
#     }
#
#     url1 = "https://api.digitalocean.com/v2/droplets"
#     url2 = "https://api.digitalocean.com/v2/"
#
#     # ubuntu-s-1vcpu-1gb-fra1-01
#     tag = "firstDOroplet"
#
#     json_data = {'name': "None", 'region': 'fra1', 'size': 's-1vcpu-1gb', 'image': None,
#                  'backups': False, 'ipv6': False, 'user_data': None, 'private_networking': None, 'volumes': None,
#                  'tags': [tag,],}
#
#     response = requests.post(url1, headers=headers)
#
#
#     manager = digitalocean.Manager(token=token)
#     my_projects = manager.get_all_projects()
#     print(my_projects)
#     # return response
#     # return my_projects
#     return manager



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
    pass
    # res = request_remote_VM_Droplet_server()
    # res[0].get_all_resources()
    # print(res.status_code)
    # 15-10-2022_07-43_sell_orders.csv
    # 15-10-2022_07-44_buy_orders.csv
    # 15-10-2022_07-43_sell_orders.csv
    # 15-10-2022_07-44_buy_orders.csv
    # import settings
    # txt_file_path = settings.BITTENSOR_LOGS_TXT_FILE
    # txt_file_path = settings.BITTENSOR_TEST_LOGS_TXT_FILE

    # res1  = read_txt_file(txt_file_path)
    # 15/10/2022 07:43 | BUY 28 | SELL 54 | TOTAL 82

    # update_orders_download_logs(txt_file_path, "15/10/2022 07:45 | BUY 28 | SELL 54 | TOTAL 82")
    # update_orders_download_logs(txt_file_path, "15/10/2022 07:46 | BUY 29 | SELL 52 | TOTAL 81")
    # update_orders_download_logs(txt_file_path, "15/10/2022 07:47 | BUY 25 | SELL 59 | TOTAL 84")
    #
    # res2 = read_txt_file(txt_file_path)



# bittensor_otc_exchange_data_download_logs.txt