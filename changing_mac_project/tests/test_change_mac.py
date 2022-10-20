
from script_mac_address import read_file


def test_change_mac():

    test_data = '22:22:11:33:44:11'
    assert test_data == read_file('testfile.txt')

