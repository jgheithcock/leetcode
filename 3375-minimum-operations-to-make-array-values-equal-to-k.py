# 3375. Minimum Operations to Make Array Values Equal to K
# From: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k

"""
Insight:

If k is > the smallest element in nums, you can never reduce.
You will need p passes for each unique number. (As, if you have i > j > k,
k is not a valid number (as i and j are greater).

Approach: walk through array, counting unique numbers, return -1 if i < k.
If k is in set, return count - 1, otherwise, return count.
"""

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set()
        for n in nums:
            if n < k:
                return -1
            unique.add(n)
        return len(unique) - (1 if k in unique else 0)

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[5,2,5,4,5], 2], 2],
    [[[2,1,2], 2], -1],
    [[[9,7,5,3], 1], 4],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
