# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary

"""
Description:
In an alien language, surprisingly, they also use English lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of 
lowercase letters.

Given a sequence of words written in the alien language, and the order of the 
alphabet, return true if and only if the given words are sorted 
lexicographically in this alien language.

Note: shorter words are ordered first if all other letters are equal.
(So, '' < 'a'-'z')

Example:
["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
True as 'h' comes before 'l' in this dictionary.

Intuition:
Step through letters, checking occurrence in order, return false if a < b.
(Use order.index(char))
"""

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compareWords(w1, w2):
            for c1, c2 in zip(w1, w2):
                if order.index(c1) < order.index(c2): return True
                if order.index(c1) > order.index(c2): return False
            return len(w1) <= len(w2) # shorter words come first
        
        for ndx in range(len(words) - 1):
            w1, w2 = words[ndx:ndx+2]
            if not compareWords(w1, w2): return False
            
        return True
        
    # from https://leetcode.com/u/ashishpawar517/
    # https://leetcode.com/problems/verifying-an-alien-dictionary/solutions/801754/python-one-liner-just-sort-the-list-acco-7ctw/
    def isAlienSortedAashish(self, words: List[str], order: str) -> bool:
            return words == sorted(words,key=lambda word:[order.index(c) for c in word])

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"], True],
    [[["hello","hello"], "abcdefghijklmnopqrstuvwxyz"], True],
    [[["word","world","row"], "worldabcefghijkmnpqstuvxyz"], False],
    [[["apple","app"], "abcdefghijklmnopqrstuvwxyz"], False],
    [[["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"],
      "zkgwaverfimqxbnctdplsjyohu"], False]
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)