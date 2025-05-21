# 3337. Total Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii

"""
Description:

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 109
nums.length == 26
1 <= nums[i] <= 25
"""

from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        f = [0] * 26 # frequencies of letters 'a' to 'z'
        for c in s:
            f[ord(c) - ord('a')] += 1
            
        for _ in range(t):
            nxt = [f[-1]] + f[:-1] # all frequencies advance 1
            for cdx in range(26):
                if f[cdx] > 0:
                    if nums[cdx] - 1 > 0:
                        for ndx in range(nums[cdx] - 1):
                            nxt[(26 + cdx + ndx + 2)%26] += f[cdx] * (nums[cdx] - 1)
            f = nxt
            
        return sum(f) % (10**9 + 7)

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [["abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]], 7],  # z -> ab
    [["azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]], 8],  # a -> bc, b -> cd, ...
    [["u", 5, [1,1,2,2,3,1,2,2,1,2,3,1,2,2,2,2,3,3,3,2,3,2,3,2,2,3]], 55],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
