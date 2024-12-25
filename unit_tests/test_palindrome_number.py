import pytest
from palindrome_number import PalindromeNumberSolution

@pytest.fixture
def solution():
    return PalindromeNumberSolution()

def test_is_palindrome1_positive_palindrome(solution):
    assert solution.is_palindrome1(121) == True

def test_is_palindrome1_positive_non_palindrome(solution):
    assert solution.is_palindrome1(123) == False

def test_is_palindrome1_negative_number(solution):
    assert solution.is_palindrome1(-121) == False

def test_is_palindrome1_single_digit(solution):
    assert solution.is_palindrome1(7) == True

def test_is_palindrome2_positive_palindrome(solution):
    assert solution.is_palindrome2(121) == True

def test_is_palindrome2_positive_non_palindrome(solution):
    assert solution.is_palindrome2(123) == False

def test_is_palindrome2_negative_number(solution):
    assert solution.is_palindrome2(-121) == False

def test_is_palindrome2_single_digit(solution):
    assert solution.is_palindrome2(7) == True