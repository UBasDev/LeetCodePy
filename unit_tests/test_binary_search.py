import pytest

from binary_search import BinarySearchSolution

@pytest.fixture
def search_instance() -> BinarySearchSolution:
    return BinarySearchSolution()

def test_element_found(search_instance):
    assert search_instance.binary_search([1, 3, 5, 7, 9], 5) == 2
    assert search_instance.binary_search([10, 20, 30, 40, 50], 10) == 0
    assert search_instance.binary_search([-10, -5, 0, 5, 10], 10) == 4

def test_element_not_found(search_instance):
    assert search_instance.binary_search([1, 3, 5, 7, 9], 6) == -1
    assert search_instance.binary_search([2, 4, 6, 8, 10], 5) == -1
    assert search_instance.binary_search([-10, -5, 0, 5, 10], -6) == -1

def test_empty_list(search_instance):
    assert search_instance.binary_search([], 5) == -1

def test_single_element_list(search_instance):
    assert search_instance.binary_search([5], 5) == 0
    assert search_instance.binary_search([5], 3) == -1

def test_search_first_last_element(search_instance):
    assert search_instance.binary_search([1, 2, 3, 4, 5], 1) == 0  # First element
    assert search_instance.binary_search([1, 2, 3, 4, 5], 5) == 4  # Last element

def test_duplicates_in_list(search_instance):
    assert search_instance.binary_search([1, 2, 2, 2, 3, 4, 5], 2) in [1, 2, 3]  # Any index where 2 appears

def test_number_outside_range(search_instance):
    assert search_instance.binary_search([10, 20, 30, 40, 50], 5) == -1  # Too small
    assert search_instance.binary_search([10, 20, 30, 40, 50], 60) == -1  # Too large
