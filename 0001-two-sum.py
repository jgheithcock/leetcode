# 1. Two Sum
# From: https://leetcode.com/problems/two-sum/

"""
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
 use the same element twice.

You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # remove any elements > target (to reduce search) then sort (log(n))
        sorted_nums = sorted(nums) # preserve nums for finding later
        
        # Start i at begining and j at end, incrementing i if too small, 
        # decrementing j if too big
        i, j = 0, len(sorted_nums) - 1
        while (i < j and sorted_nums[i] + sorted_nums[j] != target):
          if (sorted_nums[i] + sorted_nums[j] > target):
            j -= 1
          else:
            i += 1
        
        # find original i, j in nums
        found_i, found_j = sorted_nums[i], sorted_nums[j]
        i, j, k = -1, -1, 0
        while i < 0 or j < 0:
            if i < 0 and nums[k] == found_i:
                i = k
            elif nums[k] == found_j:
                j = k
            k += 1 # We would need to test k < len(nums) if no answer was possible
        return [i, j]

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[2,7,11,15], 9], [1,2]],
    [[[3,2,4], 6], [1,2]],
    [[[3,3], 6], [0,1]],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
        