import pytest
from calc_core import calc

def test_add():
    assert calc('2+2') == 4.0
def test_sub():
    assert calc('10-4') == 6.0
def test_negative_result():
    assert calc('-5-3') == -8.0
def test_mul():
    assert calc('3*4') == 12.0
def test_div():
    assert calc('10/4') == 2.5
def test_comma():
    assert calc('3,5*2') == 7.0
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError, match='Деление на ноль'):
        calc('5/0')
def test_empty():
    with pytest.raises(ValueError):
        calc('')
def test_no_operation():
    with pytest.raises(ValueError):
        calc('abc')
def test_float_precision():
    assert calc('0.1+0.2') == pytest.approx(0.3)
def test_negative_left():
    assert calc('-5+3') == -2.0
def test_spaces():
    assert calc(' 2 + 2 ') == 4.0
def test_message_empty():
    with pytest.raises(ValueError, match='Пустое'):
        calc('')