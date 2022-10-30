# test_vps_pkg


## Sources
- [Automating and Scheduling python script as Cronjobs in Ubuntu.
](https://medium.com/analytics-vidhya/automating-and-scheduling-python-script-as-cronjobs-in-ubuntu-6b31fdbce3d1)
- [How to Connect to Droplets with SSH 
](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/)
- [Basic overview of SSH Keys
](https://www.ssh.com/academy/ssh-keys)
- [What is an SSH Key?](https://www.atlassian.com/git/tutorials/git-ssh)
- [Lessons Learned: Digital Ocean for Python 3
](https://towardsdatascience.com/lessons-learned-digital-ocean-for-python-3-e2442db4246f)
- https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e
- https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e
- https://medium.com/analytics-vidhya/automating-and-scheduling-python-script-as-cronjobs-in-ubuntu-6b31fdbce3d1




## Notes

### Crontab Instructions

1. Run the following crontab command    
`crontab -e`
2. Then go to the end of the newly opened file and enter **Insert** mode by pressing `i`
3. Now add the following the line of:     
`*/1 * * * * /usr/bin/python3 /home/<user_name>/test_vps_pkg/main.py`
4. Now press `Esc` and then type `:wq` (yes, type those 3 characters) and then click `Enter`

## Managing Digital Ocean Droplet's

Recall that Digital Ocean (DO) _Droplets_ are...

> are Linux-based virtual machines (VMs) that run on top of virtualized hardware. Each Droplet you create is a new server you can use, either standalone or as part of a larger, cloud-based infrastructure.

DO Droplets are managed via a terminal & SSH. As such, this requires either a terminal with a built-in SSH client or just simply an SSH client. Optionally although highly advisable is to also have an **SSH key pair**!

Client authentication can be achieved via either the use of passwords or SSH keys. The later of the two being significantly more secure

Connecting to a Droplet via SSH requires 3 pieces of info:
1. Droplet's IP address.
2. The default username on the Droplet remote server. The default username is `root` on most operating systems, like Ubuntu and CentOS.
3. The default password for the above corresponding default user **IF** that is the case that SSH keys are not being used.

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


## Steps

### 1) `ssh` into your Droplet virtual machine server

Syntax:

```ssh <user_name>>@<IP_address_ipv4>```

Example:

```ssh xav@207.154.227.72```

---

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


---

```bash
$ crontab -e
```

Add within Vim to this file the now following (i):
```
*/1 * * * * /usr/bin/python3 /home/xav/test_vps_pkg/main.py
```

Press `Esc` and then type `:wq` and hit enter.

Now check to see if this worked via the following:
```bash
crontab -l
```

Count the number of files in a directory
```bash
ls <path_to_or_name_of_directory> -1 | wc -l
```

Size of a directory
```bash
du -h <path_to_or_name_of_directory>
```

```bash
pwd
```
> Returns -> /home/xav/test_vps_pkg

```bash
cat logs/bittensor_otc_exchange_data_download_logs.txt
```

```bash
cat logs/bittensor_otc_exchange_data_download_logs.txt | cut -d ' ' -f 11
```

Compute the SUM of TOTALS of each row in bittensor_otc_exchange_data_download_logs.txt
```bash
cat logs/bittensor_otc_exchange_data_download_logs.txt | cut -d ' ' -f 11 | paste -s -d+ - | bc
```
Get total number of rows in otc_exchange_data/cmplt_orders_dataset/sell_orders.csv
```bash
cat data/bittensor/otc_exchange_data/cmplt_orders_dataset/sell_orders.csv | wc -l
```


FILENAMESELLS="data/bittensor/otc_exchange_data/cmplt_orders_dataset/sell_orders.csv"
FILENAMEBUYS="data/bittensor/otc_exchange_data/cmplt_orders_dataset/buy_orders.csv"

sells=$(cat $FILENAMESELLS | wc -l)
buys=$(cat $FILENAMEBUYS | wc -l)

sum=$(($sells + $buys));
echo $sum





*/1 * * * * /usr/bin/python3 /home/xav/test_vps_pkg/main.py


total_count=0

FILENAME="logs/bittensor_otc_exchange_data_download_logs.txt"

LINES=$(cat $FILENAME)

for TICK in $LINES
do
    echo "TICK"
    tick_OB_total=${TICK: -2}
    echo $x_value-$y_value | bc
    total_count=total_count+tick_OB_total
done


cat logs/bittensor_otc_exchange_data_download_logs.txt | cut -d ' ' -f 9 | paste -sd+ | bc -l


## Misc

[//]: # (scp -r xav@10.10.0.1:/remote/directory/new_image.png /local/directory)





