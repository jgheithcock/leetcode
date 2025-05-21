#!/usr/bin/env python3

# 368. Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset

"""
Intuition:

Initially, I thought I could just step through with two loops and aggregate
but I now see I need to look at all subsets, as in "1863. Sum of All Subset XOR Totals"

The challenge is that this is O(2^N) time.

A faster method is to use dynamic programing:
Create an array for each element, that will hold the count if that was the last
element in your answer. A second array, `prev`, will hold the index to the previous
element in the best case answer.

[1, 2, 3, 4, 9, 8, 27, 16] -> [1, 2, 4, 8, 16] vs [1, 3, 9, 27]
[2,3,4,5,7,8,14,21,28,35,49,343,2401] -> [7, 49, 343, 2401]
"""

from typing import List

class Solution:
	def largestDivisibleSubsetTreeVersion(self, nums: List[int]) -> List[int]:
		def dfs(nums, best=[]):
			if len(nums) == 0:
				return best
			candidate, remainder = nums[:1], nums[1:]
			def dividesAll(candidate, arr):
				for n in arr:
					if n % candidate != 0 and candidate % n != 0:
						return False
				return True
			temp = dfs(remainder, best + candidate) if dividesAll(candidate[0], best) else []
			temp2 = dfs(remainder, best) # without candidate
			if len(temp) > len(temp2):
				return temp
			return temp2
		return dfs(nums)

	def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
		if not nums: # handle empty nums case so we always have at least 1
			return []
			
		# first sort the array so we only need to test in one direction
		nums.sort()
		n = len(nums)
		cnts = [1] * n  # 1 as the element itself is length 1
		prev = [-1] * n # -1 used as a sentinal
		
		max_len = 1
		max_indx = 0
		
		for i in range(1, n): # Note 0 < i < n
			for j in range(i): # Note 0 <= j < i
				if nums[i] % nums[j] == 0 and cnts[j] + 1 > cnts[i]:
					# j divides i and adding j will extend the current best for i
					cnts[i] = cnts[j] + 1
					prev[i] = j # recording previous index for reconstruction
			if cnts[i] > max_len:
				max_len = cnts[i]
				max_idx = i
		
		# max_idx now holds the index to the last best element
		# Walk backwards using the elements in prev
		result = []
		while max_idx != -1:
			result.append(nums[max_idx])
			max_idx = prev[max_idx]
		
		return result[::-1] # reverse to have correct order

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
	[[[1,2,3]], [1,3]],
	[[[1,2,4,8]], [1,2,4,8]],
	[[[2,3,4,5,7,8,14,21,28,35,49,343,2401]], [7,49,343,2401]]
]

if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
