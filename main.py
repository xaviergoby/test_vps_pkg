import numpy as np
from test_pkg_module import test_pkg_module_script

def print_numpy_pkg_version():
    np_pkg_ver = np.__version__
    np_pkg_ver_info_str = f"Numpy version: {np_pkg_ver}"
    return np_pkg_ver_info_str





if __name__ == "__main__":
    print(print_numpy_pkg_version())
    print(test_pkg_module_script.print_python_ver())
    print(test_pkg_module_script.msg_for_bbz())