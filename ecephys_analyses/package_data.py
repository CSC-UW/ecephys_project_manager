import os

PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DATA_DIRECTORY = os.path.join(PACKAGE_DIRECTORY, "package_data")


def package_datapath(filename):
    return os.path.join(PACKAGE_DATA_DIRECTORY, filename)