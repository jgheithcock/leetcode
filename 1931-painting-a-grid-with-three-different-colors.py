# 1931. Painting a Grid With Three Different Colors
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors


"""
Intuition

Arbitrarily, assign the colors numbers 0-2. Arbitrarily, we can choose to paint
square 0,0 color 0 each time, then multiply the resulting answer by three.

Given [0,0] is 0, [0,1] and [1,0] must be 1 and 2 or 2 and 1 and [1,1], if in the space
must be 0. Hmm, then it starts to blow up.

From the hints, we can generate all combos for a given column length (classic take/skip)
Use bitmap and AND == 0 to test validity. DP state (currentCell, prevColumn) (Hmm, a 
comment suggests (currentColumn, prevColumn)). Note constraint of m <= 5 (where m is rows). Thus, max number of entries = 3 * 2 * 2 * 2 * 2 = 48

"""

from collections import defaultdict

class Column:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def valid(self, m):
        if not (self.r & self.g == self.r & self.b == self.g & self.b == 0):
            return False
        return (self.r | self.g | self.b) == (1 << m) -1
    def validNeighbor(self, n):
        # self.r & neighbor.r == 0 if no colors in common
        return self.r & n.r == self.g & n.g == self.b & n.b == 0
    def __str__(self):
        return f"({self.r:b},{self.g:b},{self.b:b})"
    def __repr__(self):
        return f"({self.r:b},{self.g:b},{self.b:b})"

all_columns = [None] * 6
all_dp = defaultdict(int)
all_valid = [{}] * 6

def make_cols(m, n = None, r = 0, g = 0, b = 0, last = ''):
    if n == None:
        n = m - 1
    if n < 0:
        if not all_columns[m]:
            all_columns[m] = [Column(r, g, b)]
        else:
            all_columns[m].append(Column(r, g, b))
        return
    if last != 'r':
        make_cols(m, n - 1, r | 1 << n, g, b, 'r')
    if last != 'g':
        make_cols(m, n - 1, r, g | 1 << n, b, 'g')
    if last != 'b':
        make_cols(m, n - 1, r, g, b | 1 << n, 'b')

for m in range(1, 5+1):
    make_cols(m)
    valid_cols = all_columns[m]
    valid_neighbors = all_valid[m]
    for col in valid_cols:
        for n in valid_cols:
            if col.validNeighbor(n):
                if not col in valid_neighbors:
                    valid_neighbors[col] = [n]
                else:
                    valid_neighbors[col].append(n)
    for col in valid_cols:
        all_dp[col] = 1

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        valid_cols = all_columns[m]
        valid_neighbors = all_valid[m]
        
        # pre-flight dp for row 0
        dp = defaultdict(int)
        for col in valid_cols:
            dp[col] = 1
        
        # roll resulting values up to dp
        for _ in range(1, n):
            for col in valid_cols:
                ndp = defaultdict(int) # first time through, new_dp[col] == 0
                for prev_col in valid_neighbors[col]:
                    ndp[col] = (ndp[col] + dp[prev_col]) % MOD
                dp = ndp # Rolling dp
        return sum(dp.values()) % MOD

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[1, 2], 6],
    [[2, 2], 18],
    [[3, 3], 246],
    [[5, 5], 580986],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)

            
        
        
        
        