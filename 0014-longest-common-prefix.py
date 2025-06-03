'''
Leetcode problem 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.




Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        prfx = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prfx
            prfx += first[i]
        return prfx

    def longestCommonPrefixAll(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        shortest = strs[0]
        prfx = ""
        for i in range(1, len(shortest) + 1):
            test = shortest[:i]
            if all(word.startswith(test) for word in strs):
                prfx = test
            else:
                return prfx
        return prfx


TEST_CASES = [
    [[["flower","flow","flight"]],"fl"],
    [[["dog","racecar","car"]],""]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
