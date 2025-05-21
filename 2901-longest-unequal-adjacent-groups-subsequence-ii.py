# 2901. Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii

"""
Description:
(Medium)
You are given a string array words, and an array groups, both arrays having 
length n.

The hamming distance between two strings of equal length is the number of 
positions at which the corresponding characters are different.

You need to select the longest subsequence from an array of indices 
[0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1]
having length k, the following holds:

For adjacent indices in the subsequence, their corresponding groups are unequal,
i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
words[ij] and words[ij+1] are equal in length, and the hamming distance between 
them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
Return a string array containing the words corresponding to the indices (in 
order) in the selected subsequence. If there are multiple answers, return any 
of them.

Note: strings in words may be unequal in length.

Constraints:
1 <= n == words.length == groups.length <= 1000
1 <= words[i].length <= 10
1 <= groups[i] <= n
words consists of distinct strings.
words[i] consists of lowercase English letters.

Intuition:
Seems very like the 'brainpower' question, and so a dp solution using
reverse iteration.

Further Notes: Reverse iteration fails when the last elements are not as good
as the first, and prevent the earlier ones from being picked up. While I might
get around this, the editorial uses forward iteration and so....
"""

from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def validPair(i, j):
            wi, wj = words[i], words[j]
            if len(wi) != len(wj):
                return False
            if groups[i] == groups[j]:
                return False
            if sum([wi[i] != wj[i] for i in range(len(wj))]) != 1:
                return False
            return True
            
        def reconstructBest():
            solution = []
            ndx = best
            while ndx >= 0: # prior[0] == -1
                solution.append(words[ndx])
                ndx = prior[ndx]
            solution.reverse()
            return solution
        
        num = len(words)
        dp = [1] * num # dp always at least 1 if taken
        prior = [-1] * num # -1 is skip, otherwise, index to prior word
        best = 0 # dp[best] will be maximal and last word in solution

        for idx in range(num):
            for jdx in range(idx):
                # if dp[jdx] would be an improvement to what we have seen prior
                # and it is a valid pair, record new better value
                if dp[jdx] + 1 > dp[idx] and validPair(idx, jdx):
                    dp[idx] = dp[jdx] + 1
                    prior[idx] = jdx
                # else leave dp[idx] with either '1' or previous best
                
            # record if we beat prior all-time best
            if dp[idx] > dp[best]:
                best = idx
            
        return reconstructBest()
    
    def getWordsInLongestSubsequenceV1(self, words: list[str], groups: list[int]) -> list[str]:
        def canTake(i, j):
            # True if 1) words same length, 2) ham is 1, 3) groups are different
            wi, wj = words[i], words[j]
            return (
                len(wi) == len(wj)
                and sum([wi[i] != wj[i] for i in range(len(wj))]) == 1
                and groups[i] != groups[j]
                #and best[j] >= 0
            )
            
        def reconstructBest():
            solution = []
            ndx = 0
            while ndx < num:
                if best[ndx] > 0:
                    solution.append(words[ndx])
                    ndx = best[ndx]
                else:
                    ndx += 1
            return solution
        
        print(words)
        num = len(words)
        # create dp and best with +1 words to handle edge case at end
        dp = [0] * (num + 1) # best value if we keep this word
        best = [-1] * (num + 1) # -1 is skip, otherwise, index to next word
        
        for ndx in range(num - 1, -1, -1):
            # what is the next word we can take if we take this one?
            jdx = ndx + 1
            while jdx < num:
                if canTake(ndx, jdx):
                    break
                jdx += 1
            take_len = 1 + (dp[jdx] if jdx < num else 0)
            skip_len = dp[ndx+1]
            print(f"{ndx=}, {jdx=}, {take_len=}, {skip_len=}")
            
            
            # record best length for ndx (and if taking it or not)
            if take_len >= skip_len: # default to taking
                dp[ndx] = take_len
                best[ndx] = jdx
                print(f"{words[ndx]} and {words[jdx] if jdx < num else 'None'}, {take_len=}, {skip_len=}")
                print(best)
                
            else: # best is to skip
                dp[ndx] = skip_len
        return reconstructBest()

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[["bab","dab","cab"], [1,2,2]], ["bab", "dab"]],
    [[["a","b","c","d"], [1,2,3,4]], ["a","b","c","d"]],
    [[["adbe","acace"], [2,2]], ['adbe']],
    [[["ac","caa","cda","ba"], [3,1,2,3]], ["caa","cda"]],
    [[["aab","cab","ba","dba","daa","bca"], [4,3,4,6,4,3]], ["aab","cab"]],
    [[["cc","dcd","dac","dc","ac","ad","bbb","cbb"], [7,7,2,5,4,1,6,2]], ["cc","dc","ac","ad"]],
    [[["cb","dc","ab","aa","ac","bb","ca","bcc","cdd","aad","bba","bc","ddb"], 
      [12,6,10,11,4,8,9,11,2,11,3,2,5]], ["cb","ab","aa","ac","bc"]]
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)

            