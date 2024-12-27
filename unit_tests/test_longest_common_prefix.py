import pytest
from longest_common_prefix import LongestCommonPrefixSolution

@pytest.fixture
def solution():
    return LongestCommonPrefixSolution()

def test_longest_common_prefix_common_prefix(solution):
    assert solution.longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'

def test_longest_common_prefix_no_common_prefix(solution):
    assert solution.longest_common_prefix(['dog', 'racecar', 'car']) == ''

def test_longest_common_prefix_single_string(solution):
    assert solution.longest_common_prefix(['single']) == 'single'

def test_longest_common_prefix_one_string_is_prefix(solution):
    assert solution.longest_common_prefix(['prefix', 'prefixes', 'pre']) == 'pre'

def test_longest_common_prefix2_common_prefix(solution):
    assert solution.longest_common_prefix2(['flower', 'flow', 'flight']) == 'fl'

def test_longest_common_prefix2_no_common_prefix(solution):
    assert solution.longest_common_prefix2(['dog', 'racecar', 'car']) == ''

def test_longest_common_prefix2_single_string(solution):
    assert solution.longest_common_prefix2(['single']) == 'single'

def test_longest_common_prefix2_one_string_is_prefix(solution):
    assert solution.longest_common_prefix2(['prefix', 'prefixes', 'pre']) == 'pre'