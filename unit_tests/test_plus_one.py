import pytest
from plus_one import PlusOneSolution

@pytest.fixture
def solution():
    return PlusOneSolution()

def test_plus_one_no_carry(solution):
    assert solution.plus_one([1, 2, 3]) == [1, 2, 4]

def test_plus_one_with_carry(solution):
    assert solution.plus_one([1, 2, 9]) == [1, 3, 0]

def test_plus_one_additional_digit(solution):
    assert solution.plus_one([9, 9, 9]) == [1, 0, 0, 0]

def test_plus_one_single_digit(solution):
    assert solution.plus_one([5]) == [6]

def test_plus_one_all_nines(solution):
    assert solution.plus_one([9, 9]) == [1, 0, 0]
    
def test_plus_one_no_carry(solution):
    assert solution.plus_one2([1, 2, 3]) == [1, 2, 4]

def test_plus_one_with_carry(solution):
    assert solution.plus_one2([1, 2, 9]) == [1, 3, 0]

def test_plus_one_additional_digit(solution):
    assert solution.plus_one2([9, 9, 9]) == [1, 0, 0, 0]

def test_plus_one_single_digit(solution):
    assert solution.plus_one2([5]) == [6]

def test_plus_one_all_nines(solution):
    assert solution.plus_one2([9, 9]) == [1, 0, 0]