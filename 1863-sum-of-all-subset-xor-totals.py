#!/usr/bin/env python3

# 1863. Sum of All Subset XOR Totals
# From: https://leetcode.com/problems/sum-of-all-subset-xor-totals

"""
Intuition

First we will need a method for enumerating subsets of an array. The answer is then
just to iterate over them, adding the xorTotal for each.

From the examples, they start with the empty array and branch at each spot, either
adding the element or skipping. Thus, a recursive solution where you build a binary
tree, based on 0-skip element, or 1-add element, will cover this. While you could
first build the tree and then traverse it, you never need the tree and so can traverse
a virtual one.

Approach

Create a dfs tree search that takes the nums left and the current subset.
If nums left is empty, return xorTotal of subset, otherwise, create a new subset
with the first element from nums, remove the first element from nums, then
return dfs(reducedNums, originalSubset) + dfs(reducedNums, newSubset).

e.g.
nums = [7, 2, 4, 6]
return dfs([2,4,6],[]) + dfs([2,4,6],[7])

Time and Space Complexity:

Traversing a binary tree is O(M), where M is the number of elements, in this case
number of subsets. As each element in `nums` creates two sets, there are 2^N (where
N is the number of elements in `nums`). So our traversal is O(2^N). For each subset,
computing xorTotal is O(N) (as you go through each element) and so the total overall
is O(N * 2^N).

Space complexity is O(N) as you need to recurse for each element.

Altering `dfs` to take and pass on a running total means you can remove the call
to xorTotal at the end and have dfs() pass total ^ newSubset[0] for that case,
reducing time complexity to O(2^N).

O(n) Approach:

As each element in `nums` is in half of the subsets, half is 2^(N-1). As a thought
experiment, posit that for a given bit (say the zeroth bit, e.g. 2^0 = 0001) only
one element has that bit. E.g. [1, 2, 4, 6,...] (where the rest are even numbers)
Half of the subsets do not have the 2^0 bit set and so do not contribute, the 
other half have exactly one element with that bit and so the number of `1`s we 
will contribute is 2^(N-1), or 2^(N-1) 1's.
Thus, we will have a `1` followed by N-1 zeros, which we can confirm.

If we have two elements that have a `1` bit set, we will have:

+----------+---------+--------------+
|          | No ele1 |   Has ele1   |
+----------+---------+--------------+
| No ele2  | []      | [ele1]       |
| Has ele2 | [ele2]  | [ele1, ele2] |
+----------+---------+--------------+
E.g.:
1/4th: neither elements
1/4th: first of the two
1/4th: second of the two
1/4th: both elements


In this case, the first group contributes nothing, as seen above, the last also
contributes nothing as the two elements will XOR out each other. The other two 
groups will each contribute a single element and so again, we will have 2^(N-1)
sets with a single element and again, a `1` followed by N-1 zeros.

For more elements, the same pattern will continue, where half will have either no
elements or an even number, and so not contribute, the other half will have an
odd number and so will contribute.

Thus, given an array `nums`, each bit contributes and so we can OR each element
and then multiply by 2^(N-1), which is to say, left shift (N-1).

See `onePass` below for the implementation.
"""

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xorTotal(subset):
            total = 0
            for x in subset:
                total = total ^ x
            return total

        def dfs(nums, subset=[]):
            if len(nums) == 0:
                return xorTotal(subset)
            newSubset, nums = nums[:1] + subset, nums[1:]
            return dfs(nums, subset) + dfs(nums, newSubset)
        
        def onePass(nums):
            total = 0
            for num in nums:
                total |= num
            return total * (2 ** (len(nums) - 1))

        return dfs(nums)

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[1,3]], 6],  # The XOR total of [1,3] is 2, and the XOR total of [1] is 1, and the XOR total of [3] is 3, and the XOR total of [] is 0. So the sum is 2 + 1 + 3 + 0 = 6.
    [[[5,1,6]], 28],  # The XOR total of [5,1,6] is 2, and the XOR total of [5,1] is 4, and the XOR total of [5,6] is 3, and the XOR total of [1,6] is 7, and the XOR total of [5] is 5, and the XOR total of [1] is 1, and the XOR total of [6] is 6, and the XOR total of [] is 0. So the sum is 2 + 4 + 3 + 7 + 5 + 1 + 6 + 0 = 28.
    [[[3,4,5,6,7,8]], 480],  # The XOR total of all subsets is 480
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
