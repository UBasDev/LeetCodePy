import pytest
from two_sum import TwoSumSolution

@pytest.fixture
def solution():
    return TwoSumSolution()

def test_two_sum1_valid_pair(solution):
    assert solution.two_sum1([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum1_no_pair(solution):
    assert solution.two_sum1([1, 2, 3, 4], 8) == []

def test_two_sum1_empty_list(solution):
    assert solution.two_sum1([], 5) == []

def test_two_sum1_multiple_pairs(solution):
    result = solution.two_sum1([1, 3, 2, 4], 6)
    assert result == [1, 3] or result == [2, 3]

def test_two_sum2_valid_pair(solution):
    assert solution.two_sum2([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum2_no_pair(solution):
    assert solution.two_sum2([1, 2, 3, 4], 8) == []

def test_two_sum2_empty_list(solution):
    assert solution.two_sum2([], 5) == []

def test_two_sum2_multiple_pairs(solution):
    result = solution.two_sum2([1, 3, 2, 4], 6)
    assert result == [1, 3] or result == [2, 3]