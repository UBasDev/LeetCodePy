import pytest
from climbing_stairs import ClimbingStairsSolutions

@pytest.fixture
def solution():
    return ClimbingStairsSolutions()

def test_climb_stairs_n1(solution):
    assert solution.climb_stairs(1) == 1

def test_climb_stairs_n2(solution):
    assert solution.climb_stairs(2) == 2

def test_climb_stairs_n3(solution):
    assert solution.climb_stairs(3) == 3

def test_climb_stairs_n4(solution):
    assert solution.climb_stairs(4) == 5

def test_climb_stairs_n5(solution):
    assert solution.climb_stairs(5) == 8

def test_climb_stairs_large_n(solution):
    assert solution.climb_stairs(10) == 89
    assert solution.climb_stairs(20) == 10946