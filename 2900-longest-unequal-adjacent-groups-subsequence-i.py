# 2900. Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i

"""
Intuition:
Seems you can just make two passes, one starting at 0, the other at 1
Case 1: 0,1,0,1,0,1,1 -> (starting at 0) 0,1,0,1,0,1
Case 2: 1,1,0,1,0,1,0 -> (starting at 1) (same)
Starting at that point, delete any i, where g[i-1] == g[i].

Oh, you don't even need to skip as, in case 2, deleting g[1] gives the same result

(A greedy algorithm)

Notes: Did in their web page and then copied results.

"""

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(groups)):
            if groups[i-1] != groups[i]:
                result.append(words[i])
        return result