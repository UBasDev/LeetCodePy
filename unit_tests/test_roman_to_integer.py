import pytest
from roman_to_integer import RomanToIntegerSolution

@pytest.fixture
def solution():
    return RomanToIntegerSolution()

def test_roman_to_integer1_single_numeral(solution):
    assert solution.roman_to_integer1('I') == 1
    assert solution.roman_to_integer1('V') == 5
    assert solution.roman_to_integer1('X') == 10
    assert solution.roman_to_integer1('L') == 50
    assert solution.roman_to_integer1('C') == 100
    assert solution.roman_to_integer1('D') == 500
    assert solution.roman_to_integer1('M') == 1000

def test_roman_to_integer1_no_subtraction(solution):
    assert solution.roman_to_integer1('III') == 3
    assert solution.roman_to_integer1('VIII') == 8
    assert solution.roman_to_integer1('LVIII') == 58

def test_roman_to_integer1_with_subtraction(solution):
    assert solution.roman_to_integer1('IV') == 4
    assert solution.roman_to_integer1('IX') == 9
    assert solution.roman_to_integer1('XL') == 40
    assert solution.roman_to_integer1('XC') == 90
    assert solution.roman_to_integer1('CD') == 400
    assert solution.roman_to_integer1('CM') == 900

def test_roman_to_integer1_largest_numeral(solution):
    assert solution.roman_to_integer1('MMMCMXCIV') == 3994

def test_roman_to_integer1_empty_string(solution):
    assert solution.roman_to_integer1('') == 0