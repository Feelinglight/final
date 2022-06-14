from PyQt5.QtWidgets import QApplication
from ..calculator import Calculator

# content of test_sample.py
def calc(x, y, op):
    app = QApplication([])
    calculator = Calculator()

    for s in str(x):
        calculator._btnClicked(s)

    calculator._btnClicked(op)

    for s in str(y):
        calculator._btnClicked(s)

    return int(calculator.getResult())


def test_sum():
    assert calc(123, 123, '+') == 246, "bad 123 + 123 sum =("
    assert calc(1, 1, '+') == 2, "bad 1 + 1 sum =("
    assert calc(2, 2, '+') == 4, "bad 2 + 2 sum =("

def test_mul():
    assert calc(1, 1, '*') == 1, "bad 1 + 1 mul =("
    assert calc(2, 2, '*') == 4, "bad 2 + 2 mul =("
