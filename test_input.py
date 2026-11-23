import pytest
from input_utils import parse_number
def test_parse_int():
    assert parse_number('5') == 5.0
def test_parse_float():
    assert parse_number('3.14') == 3.14
def test_parse_comma():
    assert parse_number('3,5') == 3.5
def test_parse_spaces():
    assert parse_number(' 7 ') == 7.0
def test_parse_empty():
    with pytest.raises(ValueError, match='Пустой ввод'):
        parse_number('')
def test_parse_bad():
    with pytest.raises(ValueError):
        parse_number('abc')
def test_parse_inf():
    with pytest.raises(ValueError):
        parse_number('inf')