'''
Leetcode problem 2119. A Number After a Double Reversal
https://leetcode.com/problems/a-number-after-a-double-reversal/solutions/1647533/check-for-num-10/
Difficulty: Easy

Reversing an integer means to reverse all its digits.


	For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the
leading zeros are not retained.


Given an integer num, reverse num to get reversed1, then reverse reversed1 to
get reversed2. Return true if reversed2 equals num. Otherwise return false.


Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals
num.


Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not
equal num.


Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.



Constraints:


	0 <= num <= 106



'''

from typing import List

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return str(num)[-1] != '0' or num == 0
        # Or, more simply...
        # return num == 0 || num % 10

TEST_CASES = [
    [[526],True],
    [[1800],False],
    [[0],True]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
