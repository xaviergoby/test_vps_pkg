# test_vps_pkg

## Notes


> */1 * * * * /Users/Ksavier/PycharmProjects/test_vps_pkg/venv/bin/python3 /Users/Ksavier/PycharmProjects/test_vps_pkg/main.py

## Storage Space Calculations

- One sell/buy orders csv file of data obtained is approximately 1 KB (1000 bytes).    


- Download interval = 5 minuets
  - 12 times an hour
  - 288 times a day
  - 2016 times a week      

  

- Download interval = 1 minuet
  - 60 times an hour
  - 1440 times a day
  - 10080 times a week
  - 10080 KB = 10,08 MB


## Key Info
- IP address (ipv4): 207.154.227.72

## Sample Snippets

### Copying data via ssh between a local & a remote machine

- python interpreter path: /Users/Ksavier/PycharmProjects/test_vps_pkg/venv/bin/python3
- script path: /Users/Ksavier/PycharmProjects/test_vps_pkg/main.py

```scp -r <user_name>@<IP_address_AKA_ipv4>:<path_to_remote_directory> <path_to_local_directory>```

SCP can securely copy directories and files to and from other servers.
A sample directory can be recursively copied to a distant server using the following command.
Copying the contents of a local directory to a remote directory:

```scp -r <directory_name_or_path_to_copy> <user_name>@<IP_address_AKA_ipv4>:<path_to_remote_directory>```


Running a command on your local computer to upload files to your server is pretty easy on macOS or Linux via:

```scp -r <path_to_local_files_to_copy> <root_or_username>@<IP_address_AKA_ipv4>:<path_to_the_remote_loc_to_copy_files_to>```

## CRONNTAB

```crontab -e```

Hit `i`

paste: 


## Data Description

### Buy Orders Sample Downloaded CSV Data

 `15-10-2022_07-43_buy_orders.csv` 

|  | Datetime | Prices | Volume | Total |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 15/10/2022 07:43 | 20.67 | 979.39 | 20243.93 |
| 1 | 15/10/2022 07:43 | 20.6 | 24.96 | 514.17 |
| 2 | 15/10/2022 07:43 | 20.55 | 24.8 | 509.71 |
| 3 | 15/10/2022 07:43 | 20.5 | 23.79 | 487.63 |
| 4 | 15/10/2022 07:43 | 20.5 | 100.08 | 2051.67 |
| 5 | 15/10/2022 07:43 | 20.45 | 9.98 | 204.11 |


### Sell Orders Sample Downloaded CSV Data

`15-10-2022_07-43_sell_orders.csv`


|  | Datetime | Prices | Volume | Total |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 15/10/2022 07:43 | 21.5 | 350.0 | 7525.0 |
| 1 | 15/10/2022 07:43 | 21.8 | 50.0 | 1090.0 |
| 2 | 15/10/2022 07:43 | 21.9 | 100.0 | 2190.0 |
| 3 | 15/10/2022 07:43 | 22.1 | 50.0 | 1105.0 |
| 4 | 15/10/2022 07:43 | 22.45 | 10.0 | 224.5 |


[//]: # (scp -r xav@10.10.0.1:/remote/directory/new_image.png /local/directory)

