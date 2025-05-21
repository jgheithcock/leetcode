# 3335. Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i

"""
Intuition:

Some examples:
'a' -> you would need t > 26 to get to ab
'b' -> t > 25 -> 'ab'
...
'z' -> t = 1 -> 'ab'

Thought experiment: if s => 'aa' then it seems this is just modulo 26
in that if you start with 'a' as the string, that goes to 'aa' in 26
which goes to 'aaaa' in another 26. That is, in every 26, the string
doubles.
But for 'b', the first doubling is at 25, then every 26
for 'c', first doubles at 24, then every 26
So the doubles are t // 26 + (t > (ord('z') - ord(c))) for each c

t = t - ord('z') - ord(c)
t = t // 26
doubles = t ** 2

"""

from collections import deque, Counter
from operator import itemgetter
from string import ascii_lowercase
from functools import reduce
from typing import List

class Solution:
    # The following came from a comment from LC_bruh (vokasik) who used a 
    # deque and simply brute-forced it. This is my attempt to recreate
    # using an array
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        f = [0] * 26 # frequencies of letters 'a' to 'z'
        for c in s:
            f[ord(c) - ord('a')] += 1
            
        for _ in range(t):
            f = [f[-1]] + f[:-1] # a->b, b->c, z->a
            f[1] += f[0] # 'z's that are now 'a's create extra 'b's
        return sum(f) % (10**9 + 7)
        
    # Version with Queue
    def lengthAfterTransformationsQueue(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        q = deque([0] * 26)
        oa = ord('a')
        for c in s:
            q[ord(c) - oa] += 1
            
        for _ in range(t):
            q[0] += q[25] # all z's add an 'a' (this will be the 'b' after the next line)
            q.appendleft(q.pop()) # simulates shift where a->b, b->c
        return sum(q) % MOD
            
    def lengthAfterTransformationsBAD(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        oz = ord('z')
        result = 0
        for c in s:
            offset = oz - ord(c)
            first_cycle = (t > offset)
            cycles = max(0, (t - offset) // 26)
            added = (cycles ** 2) % MOD
            result += added + first_cycle + 1 # (+1 as we get a 'b')
        return result
        
    # Maria (MikPosps) 5-line, O(n+t)
    # This is like the deque above but I like putting the 'b' increment after
    # The whole ...itemgetter... stuff seems less awesome
    def lengthAfterTransformations5Line(self, s: str, t: int) -> int:
        q = deque(itemgetter(*ascii_lowercase)(Counter(s)))
        for _ in range(t):
            q.appendleft(q.pop())
            q[1] += q[0]
        return sum(q) % (10**9 + 7)
    
    # and her 2 line, O(n + 26*t). Also does all the transforms
    def lengthAfterTransformations2Line(self, s: str, t: int) -> int:
        return sum(reduce(lambda q,_:(q[-1],q[0]+q[-1])+q[1:-1], range(t),
            itemgetter(*ascii_lowercase)(Counter(s)))) % (10**9 + 7)
    
    # Sung Jinwoo's DP solution from his writeup
    # https://leetcode.com/problems/total-characters-in-string-after-transformations-i/solutions/6738976/dp-simulation-with-images-example-walkth-3qqd/
    # While you could think about transforming the string into an array of ordinals
    # that loop is O(26) or constant, so irrelevant.
    def lengthAfterTransformationsSingJinwoo(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (t + 26)
        for i in range(26): dp[i] = 1
        for i in range(26, t + 26): dp[i] = (dp[i - 26] + dp[i - 25]) % mod
        ans = 0
        for ch in s: ans = (ans + dp[ord(ch) - ord('a') + t]) % mod
        return ans
            
    # The following uses a dp solution that precomputes all answers for each character
    # Runs in O(26) = O(1) time!
    def __init__(self):
        self.dp = [1] * (100_000 + 26)
        for i in range(26, len(self.dp)):
            self.dp[i] = (self.dp[i-26] + self.dp[i-25]) % 1_000_000_007

    def lengthAfterTransformationsPrecompute(self, s: str, t: int) -> int:
        ans = 0
        cnt = Counter(s)
        for k, v in cnt.items():
            ans = (ans + v * self.dp[(ord(k) - 97) + t]) % 1_000_000_007
        return ans

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [["a", 1], 1],  # 'a' -> 'b'
    [["a", 2], 2],  # 'a' -> 'b' -> 'c'
    [["a", 26], 2],  # 'a' -> 'b' -> ... -> 'z' -> 'ab'
    [["z", 1], 2],  # 'z' -> 'ab'
    [["abc", 2], 6],  # 'abc' -> 'bcd' -> 'cde'
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
        