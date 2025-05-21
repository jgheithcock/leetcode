# 1550. Three Consecutive Odds
# From https://leetcode.com/problems/three-consecutive-odds

"""
Description:
Given an integer array arr, return true if there are three consecutive odd 
numbers in the array. Otherwise, return false.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i, j, k in zip(range(0, n), range(1, n), range(2, n)):
            if arr[i] % 2 and arr[j] % 2 and arr[k] % 2:
                return True
        return False

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[2,6,4,1]], False],
    [[[1,2,34,3,4,5,7,23,12]], True],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
