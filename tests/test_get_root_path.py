from carte_blanche_path import get_root_path
import os


def test_get_root_path():
    _path = get_root_path()

    assert _path == os.getcwd()
