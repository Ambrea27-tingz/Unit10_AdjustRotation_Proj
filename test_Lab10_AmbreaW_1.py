"""
Pytest Test File / file name: test_Lab10_AmbreaW_1

Creating tests to validate that the code is behaving properly.

Checking for normal inputs, invalid inputs, 

and to detect bugs early in the codes development."
"""

import pytest
from Lab10_AmbreaW_1 import adjust_rotation

def test_positive_adjust_rotation_value():
    assert adjust_rotation(100) == 100

def test_more_than_360():
    assert adjust_rotation(460) == 100

def test_negative_value():
    assert adjust_rotation(-100) == 260 

def test_non_numeric():
    with pytest.raises(ValueError):
        adjust_rotation("hello")    






#run the tests file with the command:
# pytest test_Lab10_AmbreaW_1.py
#run for more detail: pytest -v test_Lab10_AmbreaW_1.py
