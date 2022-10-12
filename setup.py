from setuptools import setup

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

requirements = read_requirements("requirements.txt")

setup(
    name='test_vps_pkg',
    version='1.0',
    packages=['test_pkg_module'],
    url='https://github.com/xaviergoby/test_vps_pkg',
    license='',
    author='Xavier Goby',
    author_email='xgoby@hotmail.com',
    description='Testing cloning a Github repo and installing it on a VPS',
    install_requires=requirements
)
