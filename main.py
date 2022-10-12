import numpy as np


def print_numpy_pkg_version():
    np_pkg_ver = np.__version__
    np_pkg_ver_info_str = f"Numpy version: {np_pkg_ver}"
    return np_pkg_ver_info_str





if __name__ == "__main__":
    print_numpy_pkg_version()