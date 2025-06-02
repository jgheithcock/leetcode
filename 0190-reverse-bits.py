'''
Leetcode problem 190. Reverse Bits
https://leetcode.com/problems/reverse-bits/description/
Difficulty: Easy

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In
this case, both input and output will be given as a signed integer type. They
should not affect your implementation, as the integer's internal binary
representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement
notation. Therefore, in Example 2 above, the input represents the signed integer
-3 and the output represents the signed integer -1073741825.



Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents
the unsigned integer 43261596, so return 964176192 which its binary
representation is 00111001011110000010100101000000.


Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents
the unsigned integer 4294967293, so return 3221225471 which its binary
representation is 10111111111111111111111111111111.




Constraints:

The input must be a binary string of length 32



Follow up: If this function is called many times, how would you optimize it?

'''

from typing import List

class Solution:
    def reverseBitsStr(self, n: int) -> int:
        return int(f'{n:032b}'[::-1],2)

    def reverseBitsBit(self, n: int) -> int:
        r = 0
        for i in range(32):
            r |= (n & 1) << (31 - i)
            n >>= 1
        return r

    def reverseBits(self, n: int) -> int: # OnePass
        # Swap consecutive pairs
        n = (n & 0x55555555) << 1 | (n & 0xaaaaaaaa) >> 1
        # Swap consecutive pairs of pairs
        n = (n & 0x33333333) << 2 | (n & 0xcccccccc) >> 2
        # Swap consecutive quads
        n = (n & 0x0f0f0f0f) << 4 | (n & 0xf0f0f0f0) >> 4
        # Swap consecutive bytes
        n = (n & 0x00ff00ff) << 8 | (n & 0xff00ff00) >> 8
        # Swap consecutive pairs of bytes
        n = ((n << 16) & 0xffffffff) | (n >> 16)
        return n

        

TEST_CASES = [
    [[0b00000010100101000001111010011100], 964176192],
    [[0b11111111111111111111111111111101], 3221225471]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
