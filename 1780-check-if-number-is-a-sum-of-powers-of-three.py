'''
Leetcode problem 1780. Check if Number is a Sum of Powers of Three
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/
Difficulty: Medium

Given an integer n, return true if it is possible to represent n as the sum of
distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:

Input: n = 21
Output: false


Constraints:

1 <= n <= 107

'''

from typing import List

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def toBase(n, b):
            """Returns list of digits of n in base b"""
            if n == 0: return [0]
            digits = []
            while n:
                n, digits = n // b, [n % b] + digits
            return digits
                
        return 2 not in toBase(n, 3)
        

TEST_CASES = [
    [[12],True],
    [[91],True],
    [[21],False]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
