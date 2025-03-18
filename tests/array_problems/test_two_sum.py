import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.two_sum.solution import Solution


def test_two_sum():
    solution = Solution()
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.two_sum([3, 2, 4], 6) == [1, 2]
    assert solution.two_sum([3, 3], 6) == [0, 1]


def test_two_sum_no_solution():
    solution = Solution()
    assert solution.two_sum([1, 2, 3], 7) == []
