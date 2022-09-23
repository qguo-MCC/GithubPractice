import pytest
from models.add_int import add_int
def test_add_two_int():
    assert add_int(1,2) == 3

def test_add_two_str_int():
    with pytest.raises(AssertionError):
        add_int('1','2')

def test_add_two_floats():
    with pytest.raises(AssertionError):
        add_int(1.1,2.1)