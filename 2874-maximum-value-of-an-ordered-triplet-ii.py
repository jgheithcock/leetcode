#!/usr/bin/env python3

# Based off of:
# maximum-value-of-an-ordered-triplet (different formula)
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii

# This file uses a different formula (n[i] - n[k]) * n[j]
# to see if a similar one pass solution can be used. (Answer, yes)

"""
Intuition:

Given a fixed k, the maximal i, j will be the two largest numbers in the range of [0, k).

Approach:

Track the largest i and j values.
If n > the max j:
	n is the new max j
	i is max of either old i or old j (aka, max(maxI, oldJ))
If not, and n > the max i value:
	old j is the new i, and the new j is now n, preserving order.
"""

class Solution:
	def tripletValue(self, nums: list[int], indices: list[int]) -> int:
		# (n[i] - n[j]) * n[k]
		# return (nums[indices[0]] - nums[indices[1]]) * nums[indices[2]]
		return  (nums[indices[0]] - nums[indices[2]]) * nums[indices[1]]

	def maximumTripletValue(self, nums: list[int]) -> int:
		return self.bestMaximumTripletValue(nums)
		
	def printTriplets(self, nums: list[int], indices: list[int]):
		print(f"({nums[indices[0]]} - {nums[indices[2]]}) * {nums[indices[1]]} = {self.tripletValue(nums, indices)}")
		
	def bruteForceTripletValue(self, nums: list[int]) -> int:
		max = 0
		triplets = []
		for k in range(2, len(nums)):
			for j in range(1, k):
				for i in range(j):
					# self.printTriplets(nums, [i, j, k])
					trial = self.tripletValue(nums, [i, j, k])
					if trial > max:
						max = trial
						triplets = [i, j, k]
		if (len(triplets) > 0):
			print(f"{triplets}: ({nums[triplets[0]]} - {nums[triplets[2]]}) * {nums[triplets[1]]} = {max}")
		return max
		
	def bestMaximumTripletValue(self, nums: list[int]) -> int:
		maxTrip, maxI, maxJ = 0, 0, 0 # fails with [-10, 1, -10, -1] as it uses a fake 0 for maxI
		maximumRecorded = 0
		for ndx, n in enumerate(nums):
			if maximumRecorded > 1:
				maxTrip = max(maxTrip, (maxI - n) * maxJ)
			if n > maxJ or n > maxI:
				maxI, maxJ = max(maxI, maxJ), n
				maximumRecorded += 1
		return maxTrip


tests = [
	[[-10, 1, -10, -1], 0],
	[[22,2,30,21,0, -2, 1, 4, 5, 0], 720],
	[[5,7,8,4], 24],
    [[12, 6, 1, 2, 7], 66],
    [[1, 10, 3, 4, 19], 18],
    [[1, 2, 3], 0],
]
testsOrig = [
	[[5,7,8,4], 0],
	[[12, 6, 1, 2, 7], 77],
	[[1, 10, 3, 4, 19], 133],
	[[1, 2, 3], 0],
]
solver = Solution()
for test in tests:
	got = solver.maximumTripletValue(test[0])
	if test[1] == got:
		print(f"success: {test[0]}")
	else:
		print(f"-FAIL!-: {test[0]}: - expected: {test[1]}, got: {got}")


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

