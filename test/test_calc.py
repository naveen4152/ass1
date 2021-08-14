import sys
sys.path.insert(0,'/home/naveen/Desktop/ass1/src')

import calc


def test_cal():
    assert calc.Sum(0, 0) == 0
    assert calc.Sum(4, 4) == 8
    assert calc.Sum(2, 5) == 7
    assert calc.Sum(-2,-2) == -4
    assert calc.Sum(25, -25) == 0
    assert  calc.Sum(100000, 999999) == 1099999

def test_diff():
    assert calc.Diff(0, 0) == 0
    assert calc.Diff(2, 1) == 1
    assert calc.Diff(1, -2) == 3
    assert calc.Diff(-1, -2) == 1
    assert calc.Diff(9999, 1111) == 8888
