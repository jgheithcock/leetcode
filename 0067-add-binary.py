'''
Leetcode problem 67. Add Binary
https://leetcode.com/problems/add-binary/description/
Difficulty: Easy

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

from typing import List


class Solution:
    def addBinaryPythonic(self, a: str, b: str) -> str:
        num=bin(int(a, 2) + int(b, 2))
        return num[2:] # strips off '0b'
        # Alt which uses the format string
        return "{0:b}".format(int(a, 2) + int(b, 2))
        
    def addBinary(self, a: str, b: str) -> str:
        pad = "".join(['0'] * 10 ** 4) # Alt: use zfill(max(len(a), len(b)))
        if len(a) >= len(b):
            longer, shorter = a[::-1], b[::-1] + pad
        else:
            longer, shorter = b[::-1], a[::-1] + pad

        carry = 0
        result = ''
        for ndx in range(len(longer)): # Alt: use reverse range and skip reverse
            sum = int(longer[ndx]) + int(shorter[ndx])
            match carry + sum:
                case 0:
                    result = '0' + result
                case 1:
                    result = '1' + result
                    carry = 0
                case 2:
                    result = '0' + result
                    carry = 1
                case 3:
                    result = '1' + result
                    carry = 1
        if carry:
            return '1' + result
        return result
        
    def addBinaryLeetcode(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n) # vs pad

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1): # vs reversing a/b
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")

            carry //= 2                # simpler carry math

        if carry == 1:
            answer.append("1")
        answer.reverse()

        return "".join(answer)

TEST_CASES = [
    [["11","1"],"100"],
    [["1010","1011"],"10101"],
    [
        [
            "11001000011101111111010011101001111111110000110101000",
            "1010110011100010000110100011001101110001111001001010001100000100011111011011111"
        ],
        '1010110011100010000110100110010110001111111000011101110110000100010000010000111'
    ]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
