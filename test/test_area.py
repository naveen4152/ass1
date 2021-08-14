import sys
sys.path.insert(0,'/home/naveen/Desktop/ass1/src')

import area

def test_AOS():
    assert area.Area_square(3) == 18
    assert area.Area_square(-3) == 18
    assert area.Area_square(100) == 20000


def test_AOR():
    assert area.Area_rectangle(2, 3) == 6
    assert area.Area_rectangle(-2, 3) == -6
    assert area.Area_rectangle(-2, -3) == 6
    assert area.Area_rectangle(0, 3) == 0