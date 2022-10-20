from stud.fileworkers import read_from_file


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']

    assert test_data == read_from_file('testfile.txt')
