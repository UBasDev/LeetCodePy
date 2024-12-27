import pytest
from valid_paranthesis import ValidParanthesisSolution

@pytest.fixture
def solution():
    return ValidParanthesisSolution()

def test_is_valid_valid_parentheses(solution):
    assert solution.is_valid('()') == True
    assert solution.is_valid('()[]{}') == True
    assert solution.is_valid('{[()]}') == True

def test_is_valid_invalid_parentheses(solution):
    assert solution.is_valid('(]') == False
    assert solution.is_valid('([)]') == False
    assert solution.is_valid('{[}') == False

def test_is_valid_empty_string(solution):
    assert solution.is_valid('') == True

def test_is_valid_only_opening_parentheses(solution):
    assert solution.is_valid('(((') == False
    assert solution.is_valid('{{{') == False
    assert solution.is_valid('[[[') == False

def test_is_valid_only_closing_parentheses(solution):
    assert solution.is_valid(')))') == False
    assert solution.is_valid('}}}') == False
    assert solution.is_valid(']]]') == False

def test_is_valid_mixed_valid_invalid_parentheses(solution):
    assert solution.is_valid('()[]{') == False
    assert solution.is_valid('({[)]}') == False
    assert solution.is_valid('({[]})') == True