# 2094. Finding 3-Digit Even Numbers
# From: https://leetcode.com/problems/finding-3-digit-even-numbers

"""
Description:
You are given an integer array `digits`, where each element is a digit. The 
array may contain duplicates.

You need to find *all* the *unique* integers that follow the given requirements:

- The integer consists of the *concatenation* of *three* elements from digits
  in *any* arbitrary order.
- The integer does not have *leading zeros*.
- The integer is *even*.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the
requirements.

Return a sorted array of the unique integers.

Intuition:
I had some difficulty understanding what they were asking for. My version:
Take any three digits from the input and concatenate them together.
If it > 99 (no leading zeros) and even (last digit is even), add it.

So, it seems we should just step through the combinations and add those that
follow this rule.

Follow up:
Note MikPop's elegant one liner for testing this rule (v>0==w&1) - a bit obscure
perhaps.
Also, I think 100*v+10*u+w is more clear and probably more performant than
all the int()/join()/map() stuff I did.
"""

from itertools import combinations, permutations
from typing import List
from collections import Counter

class Solution:
    def findEvenNumbersCombAndPerms(self, digits: List[int]) -> List[int]:
        results = set()
        for combo in combinations(digits, 3):
            for trial in permutations(combo):
                if trial[0] != 0 and trial[2] % 2 == 0:
                    results.add(int("".join(map(str, trial))))
        return sorted(list(results))
        
    def findEvenNumbersJustPerms(self, digits: List[int]) -> List[int]:
        results = set()
        for trial in permutations(digits, 3):
            if trial[0] != 0 and trial[2] % 2 == 0:
                results.add(int("".join(map(str, trial))))
        return sorted(list(results))
        
    def findEvenNumbersMikPosp(self, a: List[int]) -> List[int]:
        return sorted(100*v+10*u+w for v,u,w in {*permutations(a,3)} if v>0==w&1)
        
    def findEvenNumbersMikPosp2(self, a: List[int]) -> List[int]:
        z = Counter(map(str,a))
        return [v for v in range(100,1000,2) if Counter(str(v))<=z]

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[2,1,3,0]], [102,120,130,132,210,230,302,310,312,320]],
    [[[2,2,8,8,2]], [222,228,282,288,822,828,882]],
    [[[3,7,5]], []]
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
