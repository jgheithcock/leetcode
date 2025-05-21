# 198. House Robber
# From: https://leetcode.com/problems/house-robber/

"""
Description:

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

Intuition:

Given a single house, rob it. Given two houses, rob the maximum of [0] or [1].
Given 3, rob the max of it + max2 vs max1, where max1 is the maximum already
gathered of the next house and max2 the maximum of the house after.

Approach:

A recursive solution will use O(n) space and time, an iterative solution can
make use of the fact that we only need to know the previous two maxima.
"""

from typing import List

class Solution:
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        max2 = nums[n - 1]
        max1 = max(nums[n - 2], max2)
        for ndx in range(n - 3, -1, -1):
            if nums[ndx] + max2 > max1:
                max2, max1 = max1, nums[ndx] + max2
            else: # skipping
                max2, max1 = max1, nums[ndx]
        
        return max(max1, max2)

    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for ndx in range(len(nums)):
            prev, curr = curr, max(nums[ndx] + prev, curr)
        return curr

def reconstructBest(best: list[int], nums: list[int]) -> list[int]:
    solution = []
    ndx, length = 0, len(nums)
    while ndx < length:
        if nums[best[ndx]] > 0:
            solution.append(nums[ndx])
            ndx = best[ndx] + 1
        else:
            ndx += 1
    return solution


# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[1,2,3,4]], 6],  # [1, 3]
    [[[1,2,3,1]], 4],  # [0, 2]
    [[[2,7,9,3,1]], 12],  # [0, 2, 4]
    [[[14,11,0,2]], 16],  # [14, 2]
    [[[14,13,12,11]], 26],  # [14, 12]
    [[[14,13,12,11,1,4]], 30],  # [14, 12, 4]
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
