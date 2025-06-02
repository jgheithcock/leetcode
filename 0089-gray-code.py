'''
Leetcode problem 89. Gray Code
https://leetcode.com/problems/gray-code/description/
Difficulty: Medium

An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly
one bit, and
The binary representation of the first and last integers differs by exactly one
bit.

Given an integer n, return any valid n-bit gray code sequence.

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is
[00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit


Example 2:

Input: n = 1
Output: [0,1]

Constraints:

1 <= n <= 16

Intuition:
Observe that given a solution for n = 2 ([00,01,11,10]), you can form n=3 by
appending '1' to a copy and reversing the order and appending it:
[000,001,011,010] (original soltion) + [110,111,101,100] (e.g. adding 2**(n-1))

Use an iterative solution to do this.

'''

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        grays = [0, 1]
        for x in range(1, n):
            grays.extend([r + 2 ** x for r in grays][::-1])
        return grays
        

TEST_CASES = [
    [[2],[0,1,3,2]],
    [[1],[0,1]]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
