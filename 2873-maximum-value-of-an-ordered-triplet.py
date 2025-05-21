#!/usr/bin/env python3

# 2873-maximum-value-of-an-ordered-triplet
# From Leetcode daily challenge
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

"""
Description:
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that 
i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to 
(nums[i] - nums[j]) * nums[k].

tests = [
  # Input, Expected Output
	[[12, 6, 1, 2, 7], 77],
	[[1, 10, 3, 4, 19], 133],
	[[1, 2, 3], 0],
]
"""

class Solution:
	def tripletValue(self, nums: list[int], indices: list[int]) -> int:
		# (n[i] - n[j]) * n[k]
		return (nums[indices[0]] - nums[indices[1]]) * nums[indices[2]]

	def bruteForceTripletValue(self, nums: list[int]) -> int:
		max = 0
		triplets = []
		for k in range(2, len(nums)):
			for j in range(1, k):
				for i in range(j):
					trial = self.tripletValue(nums, [i, j, k])
					if trial > max:
						max = trial
						triplets = [i, j, k]
		print(triplets)
		return max
		
	def maximumTripletValue(self, nums: list[int]) -> int:
		return self.onePassTripletValue(nums)

	def onePassTripletValue(self, nums: list[int]) -> int:
		maxTrip, maxDiff, maxEle = 0,0,0
		for n in nums:
			maxTrip = max(maxTrip, maxDiff * n)
			maxDiff = max(maxDiff, maxEle - n)
			maxEle = max(maxEle, n)
		return maxTrip


tests = [
	[[-11, -1, 2], 0],
	[[5,7,8,4], 0],
	[[12, 6, 1, 2, 7], 77],
	[[1, 10, 3, 4, 19], 133],
	[[1, 2, 3], 0],
]
solver = Solution()
for test in tests:
	got = solver.maximumTripletValue(test[0])
	print(f"{test[0]}: expected: {test[1]}, got: {got}")


### Best solution: O(n) time and space complexity:

"""
Approach 4: Greedy
Intuition
Similar to approach 3, if we fix k, then the value of the triplet is maximized
when nums[i]−nums[j] takes the maximum value. We can use imax to maintain the
maximum value of nums[i] and dmax to maintain the maximum value of 
nums[i]−nums[j]. During the enumeration of k, update dmax and imax.
"""
class BestSolution:
	def maximumTripletValue(self, nums: list[int]) -> int:
		n = len(nums)
		res, imax, dmax = 0, 0, 0
		for k in range(n):
			res = max(res, dmax * nums[k])
			dmax = max(dmax, imax - nums[k])
			imax = max(imax, nums[k])
		return res

