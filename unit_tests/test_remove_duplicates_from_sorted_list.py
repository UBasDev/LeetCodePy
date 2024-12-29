import pytest
from typing import Optional
from remove_duplicates_from_sorted_list import ListNode, RemoveDuplicatesFromSortedListSolution

@pytest.fixture
def solution():
    return RemoveDuplicatesFromSortedListSolution()

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def test_delete_duplicates_no_duplicates(solution):
    head = list_to_linked_list([1, 2, 3])
    result = solution.delete_duplicates(head)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_delete_duplicates_with_duplicates(solution):
    head = list_to_linked_list([1, 1, 2, 3, 3])
    result = solution.delete_duplicates(head)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_delete_duplicates_empty_list(solution):
    head = list_to_linked_list([])
    result = solution.delete_duplicates(head)
    assert linked_list_to_list(result) == []

def test_delete_duplicates_all_duplicates(solution):
    head = list_to_linked_list([1, 1, 1, 1])
    result = solution.delete_duplicates(head)
    assert linked_list_to_list(result) == [1]

def test_delete_duplicates_single_element(solution):
    head = list_to_linked_list([1])
    result = solution.delete_duplicates(head)
    assert linked_list_to_list(result) == [1]