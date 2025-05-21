"""
416. Partition Equal Subset Sum
From: https://leetcode.com/problems/partition-equal-subset-sum

Given an integer array nums, return true if you can partition the array into 
two subsets such that the sum of the elements in both subsets is equal or false
otherwise.

Examples:

#1: [1, 5, 11, 5] -> true ([1, 5, 5] and [11])
#2: [1, 2, 3, 5] -> false
#3: [2, 3, 4, 5] -> true ([2, 5] and [3, 4]) # Note this skips a sorted list.

Intuition: This seems like the "make all subsets" type of problem but the
decision is simpler in that it is "does this element go into a or b subset?"

Approach:

Create tree of growing two sets, each branch either moves the element to a or b.
At the end, decide if true (return) or false, continue.

Time complexity: O(n) (dfs tree traversal)

"""

from typing import List

class Solution:
    # brute force. I also didn't catch the quick test to check total sum must be even
    def canPartitionRecursion(self, nums: List[int]) -> bool:
        def dfs(nums, setA, setB, aTotal=0, bTotal=0):
            if not nums:
                return aTotal == bTotal
            candidate, nums = nums[:1], nums[1:]
            if dfs(nums, setA + candidate, setB, aTotal + candidate[0], bTotal):
                return True
            return dfs(nums, setA, setB + candidate, aTotal, bTotal + candidate[0])
        
        return dfs(nums, [], [])
  

    # Dynamic programming with 1 D array (based on AI example)
    # Time: O(n * t) (t is target)
    # Space: O(t)
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False # sum of all nums must be even
    
        target = total_sum // 2
        dp = [False] * (target + 1) # Need to dp[target]
        dp[0] = True # The empty set fullfills this

        for num in nums:
            if num > target:
                return False # no way to have a subset == target
            for j in range(target, num - 1, -1): # step backwards from target to num inclusive
                if dp[j - num]: # will always be true for j == num
                    dp[j] = True # adding num to j will also reach
                    if j == target:
                        return True # found a subset already
        return dp[target] # False for sets like [4, 2, 2, 2]
        
    # Fastest solution used a bits for the dp array with no early exits.
    # ~350 TIMES faster than the 1 D approach above ()
    # Time: O(n)
    # Space: O(1)
    def bitCanPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = 1 << 0
        for num in nums:
            dp |= dp << num # multiply by 2^num
        return (dp & (1 << target)) != 0

    def bitExitCanPartition(self, nums: List[int]) -> bool:
        # 3x faster on cases where the > target number is early in cases with n = 200
        # but slower overall by almost 15%
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = 1 << 0
        for num in nums:
            if num > target:
                return False
            dp |= dp << num # multiply by 2^num
            if (dp & (1 << target)) != 0:
                return True
        return (dp & (1 << target)) != 0


# Utility for inspecting bit version above
def printBin(n):
    print(n, ':',  bin(n)[2:].zfill(64))

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[1, 5, 11, 5], True],
    [[1, 2, 3, 5], False],
    [[2, 3, 4, 5], True],
    [[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,4,99,97], True],
    [[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,0,99,97], False],
    [[4,99,97,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100], True],
    [[0,99,97,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100], False],
    [[101, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], False],
]

if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
