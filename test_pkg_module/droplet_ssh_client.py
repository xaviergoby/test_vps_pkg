# https://tonyteaches.tech/digitalocean-api-python/
from __future__ import annotations
import paramiko
import pandas as pd
from natsort import natsorted
import settings
from typing import List



class DropletSSHClient:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        # VPS dir & file paths
        self.__main_working_dir_path = "/home/xav/test_vps_pkg"
        self.__logs_dir_path = f"{self.__main_working_dir_path}/logs"
        self.__logs_file_path = f"{self.__logs_dir_path}/bittensor_otc_exchange_data_download_logs.txt"
        self.__sell_orders_dir_path = f"{self.__main_working_dir_path}/data/bittensor/otc_exchange_data/sell_orders"
        self.__buy_orders_dir_path = f"{self.__main_working_dir_path}/data/bittensor/otc_exchange_data/buy_orders"
        # self.buy_orders_dir_path = f"{self.__buy_orders_dir_path}"
        # self.sell_orders_dir_path = f"{self.__sell_orders_dir_path}"
        self.__ssh_client = None
        # self.__connect_ssh_server()
        # SFTP session on the SSH server
        self.__sftp_client = None

    @property
    def host(self):
        return self.kwargs.get('host')

    @host.setter
    def host(self, value):
        self.kwargs['host'] = value

    @property
    def username(self):
        return self.kwargs.get('username')

    @username.setter
    def username(self, value):
        self.kwargs['username'] = value

    @property
    def password(self):
        return self.kwargs.get('password')

    @password.setter
    def password(self, value):
        self.kwargs['password'] = value

    def __repr__(self):
        info = ', '.join(f'{k}={v}' for k, v in self.kwargs.items())
        return info

    def __create_ssh_client(self):
        """
        :return: A new SFTPClient session obj
        Used to open an SFTP session across an open SSH Transport and perform remote file operations.
        Instances of this class may be used as context managers.
        """
        # ssh_client = paramiko.SSHClient()
        self.__ssh_client = paramiko.SSHClient()

    def __authenticate_ssh_server(self):
        """
        https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.set_missing_host_key_policy
        Set policy to use when connecting to servers without a known host key.
        A policy is a “policy class” (or instance thereof), namely some subclass of
        MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy,
        WarningPolicy, or a user-created subclass.
        :return:
        """
        # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh_client.load_system_host_keys()
        self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__ssh_client.load_system_host_keys()

    def __connect_ssh_server(self):
        """
        :return: A new SFTPClient session obj
        Used to open an SFTP session across an open SSH Transport and perform remote file operations.
        Instances of this class may be used as context managers.
        """
        # ssh_client = paramiko.SSHClient()
        self.__create_ssh_client()
        # https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.set_missing_host_key_policy
        # Set policy to use when connecting to servers without a known host key.
        # A policy is a “policy class” (or instance thereof), namely some subclass of
        # MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy,
        # WarningPolicy, or a user-created subclass.
        # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh_client.load_system_host_keys()
        self.__authenticate_ssh_server()
        # https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.connect
        # .connect(hostname, port=22, username=None, password=None, pkey=None, key_filename=None, timeout=None, ...)
        # Connect to an SSH server and authenticate to it. The server’s host key is checked against
        # the system host keys (see load_system_host_keys) and any local host keys (load_host_keys).
        # If the server’s hostname is not found in either set of host keys, the missing host key policy
        # is used (see set_missing_host_key_policy).
        # ssh_client.connect(self.host, username=self.username, password=self.password)
        self.__ssh_client.connect(self.host, username=self.username, password=self.password)

    def connect_ssh_client(self):
        self.__connect_ssh_server()

    def close_ssh_client(self):
        """
        Close this SSHClient and its underlying Transport.
        This should be called anytime you are done using the client object.
        :return:
        """
        self.__ssh_client.close()

    def __open_vps_sftp_client(self):
        """
        :return: A new SFTPClient session obj
        Used to open an SFTP session across an open SSH Transport and perform remote file operations.
        Instances of this class may be used as context managers.
        """
        # ssh_client.connect(self.host, username=self.username, password=self.password)
        # self.__connect_ssh_server(self.host, username=self.username, password=self.password)
        # Open an SFTP session on the SSH server.
        self.__sftp_client = self.__ssh_client.open_sftp()
        # return sftp_client

    def __close_vps_sftp_client(self):
        """
        Close the SFTP session and its underlying channel.
        :return:
        """
        self.__sftp_client.close()

    def __get_vps_sftp_client_old(self):
        """
        :return: A new SFTPClient session obj
        Used to open an SFTP session across an open SSH Transport and perform remote file operations.
        Instances of this class may be used as context managers.
        """
        ssh_client = paramiko.SSHClient()
        # https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.set_missing_host_key_policy
        # Set policy to use when connecting to servers without a known host key.
        # A policy is a “policy class” (or instance thereof), namely some subclass of
        # MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy,
        # WarningPolicy, or a user-created subclass.
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.load_system_host_keys()
        # https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.connect
        # .connect(hostname, port=22, username=None, password=None, pkey=None, key_filename=None, timeout=None, ...)
        # Connect to an SSH server and authenticate to it. The server’s host key is checked against
        # the system host keys (see load_system_host_keys) and any local host keys (load_host_keys).
        # If the server’s hostname is not found in either set of host keys, the missing host key policy
        # is used (see set_missing_host_key_policy).
        ssh_client.connect(self.host, username=self.username, password=self.password)
        # Open an SFTP session on the SSH server.
        sftp_client = ssh_client.open_sftp()
        return sftp_client

    @property
    def vps_sftp_client(self) -> paramiko.SFTPClient:
        """
        :return: The currently opened SFTPClient session obj
        """
        if self.__sftp_client is None:
            self.__open_vps_sftp_client()
            # self.__sftp_client = self.__get_vps_sftp_client()
            return self.__sftp_client
        else:
            return self.__sftp_client

    @property
    def vps_sftp_session_cwd(self) -> str | None:
        """
        https://docs.paramiko.org/en/stable/api/sftp.html#paramiko.sftp_client.SFTPClient.getcwd
        Return the “current working directory” for this SFTP session,
        as emulated by Paramiko. If no directory has been set with chdir,
        this method will return None.
        :return: str of the current working directory path if it has been set, else None
        """
        return self.vps_sftp_client.getcwd()

    def vps_cd(self, dir_path: str):
        """
        https://docs.paramiko.org/en/stable/api/sftp.html#paramiko.sftp_client.SFTPClient.chdir
        Change the “current directory” of this SFTP session.
        Since SFTP doesn’t really have the concept of a current working directory,
        this is emulated by Paramiko. Once you use this method to set a working directory,
        all operations on this SFTPClient object will be relative to that path.
        You can pass in None to stop using a current working directory.
        :param dir_path:
        :return:
        """
        self.vps_sftp_client.chdir(dir_path)

    def vps_ls(self, path=None) -> List[str]:
        """
        https://docs.paramiko.org/en/stable/api/sftp.html#paramiko.sftp_client.SFTPClient.listdir
        Return a list containing the names of the entries in the given path.

        The list is in arbitrary order. It does not include the special entries '.' and '..'
        even if they are present in the folder. This method is meant to mirror os.listdir as
        closely as possible. For a list of full SFTPAttributes objects, see listdir_attr.
        :param path:
        :return:
        """
        if path is None:
            return self.vps_sftp_client.listdir()
        else:
            return self.vps_sftp_client.listdir(path)

    def dl_sell_orders_csv_file(self, csv_file_name):
        """
        paramiko.sftp_client.SFTPClient.get(remotepath, localpath, callback=None, prefetch=True)
        Copy a remote file (remotepath) from the SFTP server to the local host as localpath.
        Any exception raised by operations will be passed through.
        This method is primarily provided as a convenience.
        :param csv_file_name: str of csv file name w/ the .csv extension, e.g. 22-10-2022_11-55_sell_orders.csv
        :return: None
        """
        remote_path = f"{self.__sell_orders_dir_path}/{csv_file_name}"
        local_path = f"{settings.SCRAPED_DATASETS_DIR}/sell_orders/{csv_file_name}"
        self.vps_sftp_client.get(remote_path, local_path)

    def dl_buy_orders_csv_file(self, csv_file_name):
        """
        paramiko.sftp_client.SFTPClient.get(remotepath, localpath, callback=None, prefetch=True)
        Copy a remote file (remotepath) from the SFTP server to the local host as localpath.
        Any exception raised by operations will be passed through.
        This method is primarily provided as a convenience.
        :param csv_file_name: str of csv file name w/ the .csv extension, e.g. 22-10-2022_11-55_buy_orders.csv
        :return: None
        """
        remote_path = f"{self.__buy_orders_dir_path}/{csv_file_name}"
        local_path = f"{settings.SCRAPED_DATASETS_DIR}/buy_orders/{csv_file_name}"
        self.vps_sftp_client.get(remote_path, local_path)

    def get_scraped_sell_orders_csv_file_names(self) -> List[str]:
        """
        https://docs.paramiko.org/en/stable/api/sftp.html#paramiko.sftp_client.SFTPClient.listdir
        Return a list containing the names of the entries in the given path.

        The list is in arbitrary order. It does not include the special entries '.' and '..'
        even if they are present in the folder. This method is meant to mirror os.listdir as
        closely as possible. For a list of full SFTPAttributes objects, see listdir_attr.
        :return:
        """
        return natsorted(self.vps_sftp_client.listdir(self.__sell_orders_dir_path))

    def get_scraped_buy_orders_csv_file_names(self) -> List[str]:
        """
        https://docs.paramiko.org/en/stable/api/sftp.html#paramiko.sftp_client.SFTPClient.listdir
        Return a list containing the names of the entries in the given path.

        The list is in arbitrary order. It does not include the special entries '.' and '..'
        even if they are present in the folder. This method is meant to mirror os.listdir as
        closely as possible. For a list of full SFTPAttributes objects, see listdir_attr.
        :return:
        """
        return natsorted(self.vps_sftp_client.listdir(self.__buy_orders_dir_path))

    def load_scraped_sell_order_csv_file(self, csv_file_name) -> pd.DataFrame:
        """
        https://docs.paramiko.org/en/stable/api/sftp.html#paramiko.sftp_client.SFTPClient.open
        Open a file on the remote server. The arguments are the same as for Python’s built-in file (aka open).
        A file-like object is returned, which closely mimics the behavior of a normal Python file object,
        including the ability to be used as a context manager.
        :param csv_file_name:
        :return:
        """
        sell_orders_csv_file_remote_path = f"{self.__sell_orders_dir_path}/{csv_file_name}"
        with self.vps_sftp_client.open(sell_orders_csv_file_remote_path) as file_obj:
            file_obj.prefetch()
            df = pd.read_csv(file_obj)
            return df

    def load_scraped_buy_order_csv_file(self, csv_file_name) -> pd.DataFrame:
        buy_orders_csv_file_remote_path = f"{self.__buy_orders_dir_path}/{csv_file_name}"
        with self.vps_sftp_client.open(buy_orders_csv_file_remote_path) as file_obj:
            file_obj.prefetch()
            df = pd.read_csv(file_obj)
            return df

    def build_sell_orders_csv_file_abs_paths(self, csv_file_name):
        return f"{self.__sell_orders_dir_path}/{csv_file_name}"

    def dl_cmplt_sell_orders_df(self):
        file_names = self.get_scraped_sell_orders_csv_file_names()
        df = pd.concat(map(self.load_scraped_sell_order_csv_file, file_names), sort=False)
        return df

    def dl_cmplt_buy_orders_df(self):
        file_names = self.get_scraped_buy_orders_csv_file_names()
        df = pd.concat(map(self.load_scraped_buy_order_csv_file, file_names), sort=False)
        return df

if __name__ == "__main__":
    import private_settings
    ssh_client = DropletSSHClient(**private_settings.DO_VPS_SSH_INFO)
    ssh_client.connect_ssh_client()
    bigSELLdf = ssh_client.dl_cmplt_sell_orders_df()
    bigBUYdf = ssh_client.dl_cmplt_buy_orders_df()


    #
    # ssh_client = DropletSSHClient(**private_settings.DO_VPS_SSH_INFO)
    # print(ssh_client)
    # # res = do_vps_ssh_client_cls.get_vps_sftp_client()
    # cwd = ssh_client.vps_sftp_client.getcwd()
    # print(cwd)
    # # ssh_client.vps_cd("test_vps_pkg")
    # print(ssh_client.vps_sftp_client.getcwd())
    # print(ssh_client.vps_ls())
    # ssh_client.dl_sell_orders_csv_file("22-10-2022_11-55_sell_orders.csv")
    # # ssh_client.dl_buy_orders_csv_file("22-10-2022_11-55_buy_orders.csv")
    # ls = ssh_client.get_scraped_sell_orders_csv_file_names()
    # lb = ssh_client.get_scraped_buy_orders_csv_file_names()
    # print(ls)
    # print(lb)
    # df = ssh_client.load_scraped_sell_order_csv_file("22-10-2022_11-55_sell_orders.csv")
    # bigSELLdf = ssh_client.dl_cmplt_sell_orders_df()
    # bigBUYdf = ssh_client.dl_cmplt_buy_orders_df()

