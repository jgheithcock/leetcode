# 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
# From: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros

"""
Description:
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers 
such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.

Constraints:

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[i] <= 106

Intuition:

First find which array has the fewest zeros, (arbitrarily, we shall say nums2) 
then the count of the non-zero elements in both, n1, n2. If num_zeros_2 is 0 
and n2 > n1, no solution is possible. Actually, generically if num_zeros_1 + n1
> num_zeros_2 + n2, no solution is possible. Otherwise, the answer is 
num_zeros_2 + n2. (as you must have at least a 1 for all of num_zeros_2).

Further, I now see that it doesn't matter which side has fewest zeros, only
that both sides have at least one. The nz1+n1 <= n2 is still a requirement.

Comments on solution:
- MikPosp (https://leetcode.com/u/MikPosp/) had a great 1 line initialization
- I also think his variable choice was better
- Also points out that I didn't need all of the cases, see V2 for changes
"""

from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # determine number of zeros and sum of arrays
        n1, nz1 = 0, 0
        for d in nums1:
            if d == 0: nz1 += 1
            else: n1 += int(d)
        n2, nz2 = 0, 0
        for d in nums2:
            if d == 0: nz2 += 1
            else: n2 += int(d)

        if nz1 == 0 and nz2 == 0:
            if n1 != n2: return -1
            return n1
        elif nz1 == 0:
            if nz2 + n2 > n1: return -1
            return n1
        elif nz2 == 0:
            if nz1 + n1 > n2: return -1
            return n2
        elif nz1 + n1 > nz2 + n2:
            return nz1 + n1
        return nz2 + n2
    
    def minSumV2(self, nums1: List[int], nums2: List[int]) -> int:
        # determine number of zeros and sum of arrays
        s1, s2, z1, z2 = sum(nums1), sum(nums2), nums1.count(0), nums2.count(0)

        if z1 == 0 and z1 < z2 + s2: return -1
        elif z2 == 0 and z2 < z1 + s1: return -1
        
        return max(z1 + s1, z2 + s2)
        
    # MikPosp's two liner, showing off an elegant initialization using .count(0)
    def minSumMikPosp(self, a: List[int], b: List[int]) -> int:
            s1, s2, z1, z2 = sum(a), sum(b), a.count(0), b.count(0)
            return -(z1==0 and s1<s2+z2 or z2==0 and s1+z1>s2) or max(s1+z1,s2+z2)

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[3,2,0,1,0], [6,5,0]], 12],
    [[[2,0,2,0], [1,4]], -1],
    [[[17,1,13,12,3,13], [2,25]], -1],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
