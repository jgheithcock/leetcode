# 2843. Count Symmetric Integers
# From: https://leetcode.com/problems/count-symmetric-integers

from typing import List

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def countSym(n):
            sym = 0
            for i in range(10, n + 1, 1):
                digits = str(i)
                l = len(digits)
                if len(digits) % 2 == 0:
                    first = sum([int(d) for d in digits[:l // 2]])
                    second = sum([int(d) for d in digits[l // 2:]])
                    if (first == second):
                        sym += 1
            return sym
        if high == low:
            return countSym(high)
        return countSym(high) - countSym(low-1)
        
# Fastest - precomputes array (and only looks at numbers from 11 up)
from array import array

m = array('H', [0]) * 10001 # Needed to know max constraint of 10**4
count = 0
for i in range(11, 10001):
    if i < 100 and i % 11 == 0:
        count += 1
    elif i > 1000:
        i0 = i % 10
        i1 = (i % 100) // 10
        i2 = (i % 1000) // 100
        i3 = i // 1000
        if i0 + i1 == i2 + i3:
            count += 1
    m[i] = count

class Solution2:
    def countSymmetricIntegers(self, l: int, h: int) -> int:
        return m[h] - m[l - 1]

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[1,100]], 9],
    [[[1200,1230]], 4],
    [[[11,12]], 1],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
