# 343. Count Number of Balanced Permutations
# From: https://leetcode.com/problems/count-number-of-balanced-permutations

"""
Intuition:
First, for a brute force, iterate through all permutations of num and increment
count by passing permutation into a `isBalanced()`

Observations:
    - if e is number of even digits, & o is number of odd digits, o = e || e+1
    - s = sum(digits of num), s must be even (Proof?)
    - Once you find one balanced perm, p. Let pe and po be the even and odd
      digits of p. Then all other balanced perms will be the distinct 
      permutations of pe + distinct permutations of po.
        Proof: switching pe[i] and po[j] will fail unless they are equal, which
        will not be a new distinct permutation. Switching pe[i] & pe[k] with j
        will break the even-odd rule (#1)
        Counterargument: What about i, j, l, m where pe[i]+pe[j] == po[l]+pl[m]? (and
        where pe[i] != po[l] or po[m]) -> Indeed, that is the case. This could 
        also be swapping three, four, etc numbers

AIs:
    - is it the permutations that kill you or the isBalanced() test (Or the iteration)
"""


from itertools import permutations
from math import factorial
from functools import lru_cache

class Solution:
    def __init__(self):
        # Precompute factorials and inverse factorials for max input size (80 digits)
        MOD = 10**9 + 7
        MAX_DIGITS = 80
        MAX_INDEX = MAX_DIGITS + 1 # 0 to 80
        
        # Calculate factorials
        self.fact = [1] * MAX_INDEX
        for i in range(1, MAX_INDEX):
            self.fact[i] = self.fact[i-1] * i % MOD
            
        # Calculate modular multiplicative inverses
        inv = [1] * MAX_INDEX
        for i in range(2, MAX_INDEX):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
            
        # Calculate inverse factorials
        self.inv_fact = [1] * MAX_INDEX
        for i in range(1, MAX_INDEX):
            self.inv_fact[i] = self.inv_fact[i-1] * inv[i] % MOD

    def countBalancedPermutationsBrute(self, num: str) -> int:
        def isBalanced(num):
            result = 0
            for i in range(0, len(num)):
                if i % 2 == 0:
                    result += int(num[i])
                else:
                    result -= int(num[i])
            return result == 0
            
        result = 0
        distinct_perms = set()
        for p in permutations(num):
            if p not in distinct_perms:
                distinct_perms.add(p)
                if isBalanced("".join(p)):
                    result += 1
            
        return result % ((10 ** 9) + 7)
    
    def countBalancedPermutationsCollect(self, num: str, dps: set) -> int:
        def isBalanced(num):
            result = 0
            for i in range(0, len(num)):
                if i % 2 == 0:
                    result += int(num[i])
                else:
                    result -= int(num[i])
            return result == 0
            
        result = 0
        distinct_perms = set()
        for p in permutations(num):
            if p not in distinct_perms:
                distinct_perms.add(p)
                if isBalanced("".join(p)):
                    odds = sorted([c for i, c in enumerate(p) if i % 2 == 0])
                    evens = sorted([c for i, c in enumerate(p) if i % 2 != 0])
                    dps.add(f'{"".join(odds)}-{"".join(evens)}')
                    result += 1
            
        return result % ((10 ** 9) + 7)
        
    def countBalancedPermutationsV1(self, num: str) -> int:
        def isBalanced(num):
            result = 0
            for i in range(0, len(num)):
                if i % 2 == 0:
                    result += int(num[i])
                else:
                    result -= int(num[i])
            return result == 0
            
        def numDistinctPermutations(s) -> int:
            # formula is n! / (r1! * r2! * ... rn!)
            # where r1 etc is the repeated counts
                    
            numerator = factorial(len(s))
            
            # find counts for each character in s
            counts = {}
            for c in s:
                if c not in counts:
                    counts[c] = 1
                else:
                    counts[c] += 1
                    
            denominator = 1
            for cnt in counts.values():
                denominator *= factorial(cnt)
            return int(numerator / denominator)
            
        result = 0
        distinct_perms = set()
        for p in permutations(num):
            if p not in distinct_perms:
                distinct_perms.add(p)
                if isBalanced("".join(p)):
                    result += 1
                    break
        
        if result == 0:
            return 0
            
        odds = [c for i, c in enumerate(p) if i % 2 == 0]
        dp_odds = numDistinctPermutations(odds)
        evens = [c for i, c in enumerate(p) if i % 2 != 0]
        dp_even = numDistinctPermutations(evens)
        
        result = (dp_odds * dp_even)
            
        return result % ((10 ** 9) + 7)

    def countBalancedPermutationsV2(self, num: str) -> int:
        def subsets_for_target(num: str, target: int, needed: int) -> list[str]:
            """Given string of digits, num, returns the list of all subsets
            whose digits sum to target. Filters out any subsets whose length
            is not equal to `needed`
            """

            @lru_cache(maxsize=128)
            def recursive_search(index, current_sum, trial, complement):
                if current_sum == target and len(trial) == needed:
                    # add any missing numbers to complement
                    missing = [num[ndx] for ndx in range(index, len(num))]
                    trial = "".join(sorted(trial))
                    complement = "".join(sorted(list(complement) + missing))
                    return [(trial, complement)]
                elif current_sum > target or len(trial) > needed or index > max_index:
                    return []

                # combine two paths, one including next digit, one without
                d = num[index]
                with_results = recursive_search(
                    index + 1, current_sum + int(d), trial + d, complement
                )
                without_results = recursive_search(
                    index + 1, current_sum, trial, complement + d
                )
                return with_results + without_results

            max_index = len(num) - 1
            results = recursive_search(0, 0, "", "")
            return list(set(results))

        @lru_cache(maxsize=128)
        def numDistinctPermutations(s) -> int:
            # formula is n! / (r1! * r2! * ... rn!)
            # where r1 etc is the repeated counts

            numerator = factorial(len(s))

            # find counts for each character in s
            counts = {}
            for c in s:
                if c not in counts:
                    counts[c] = 1
                else:
                    counts[c] += 1

            denominator = 1
            for cnt in counts.values():
                denominator *= factorial(cnt)
            return int(numerator / denominator)

        total = sum([int(d) for d in num])
        if total % 2 != 0:
            return 0  # sum of all digits must be even
        else:
            target = total // 2

        all_odds = subsets_for_target(num, target, (len(num) + 1) // 2)

        result = 0
        for odds, evens in all_odds:
            dp_odds = numDistinctPermutations(odds)
            dp_evens = numDistinctPermutations(evens)
            result += dp_odds * dp_evens

        return result % ((10**9) + 7)
        
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        digits = [int(d) for d in num]
        total = sum(digits)
        if total % 2 != 0:
            return 0
        target = total // 2
        odd_len = (n + 1) // 2 # even_len == n // 2

        # Use memoization to avoid recomputation
        from functools import lru_cache

        # Set to store unique distributions of digits between odds and evens
        unique_distributions = set()

        @lru_cache(maxsize=None)
        def dfs(i, s, k, mask):
            # Depth-first search to fill results with counts of all permutations
            # where odds and evens both sum to target
            # i - index into num for current digit
            # s - current sum
            # k - target sum
            # mask - bitmask of which indices are in the odd group
            if k < 0 or s < 0:
                return
            if i == n:
                if s == 0 and k == 0:
                    odds = [num[j] for j in range(n) if (mask & (1 << j))]
                    evens = [num[j] for j in range(n) if not (mask & (1 << j))]
                    # Sort to ensure consistent counting of repeated digits
                    odds.sort()
                    evens.sort()
                    odds_counts = [0] * 10 # frequency of each digit 0-9
                    evens_counts = [0] * 10
                    for d in odds:
                        odds_counts[int(d)] += 1
                    for d in evens:
                        evens_counts[int(d)] += 1
                    unique_distributions.add((tuple(odds_counts), tuple(evens_counts)))
                return
            # pick current digit for odds
            dfs(i + 1, s - digits[i], k - 1, mask | (1 << i))
            # don't pick current digit (goes to evens)
            dfs(i + 1, s, k, mask)

        dfs(0, target, odd_len, 0)

        total_perms = 0
        for odds_counts, evens_counts in unique_distributions:
            # For each unique distribution of digits, compute the number of distinct permutations
            perms_odds = self.multinomial_coefficient(odds_counts)
            perms_evens = self.multinomial_coefficient(evens_counts)
            # Multiply by the number of ways to achieve this distribution
            total_perms = (total_perms + perms_odds * perms_evens) % MOD

        return total_perms

    def multinomial_coefficient(self, counts):
        """Returns number of unique permutations of each digit.
        The formula for the multinomial coefficient is n! / (r0! * r1! ... r9!)
        where r0, r1 etc is count each digit is present."""
        n = sum(counts)
        result = self.fact[n] # precomputed in __init__
        for c in counts:
            result = result * self.inv_fact[c]
        return int(result)

    def countBalancedPermutationsDP(self, num: str) -> int:
        """Bottom-up DP approach to count balanced permutations.
        
        State: dp[i][s][k] represents the set of unique digit distributions
        where:
        - i: processed first i digits
        - s: sum of digits in odd positions
        - k: number of digits in odd positions
        """

        MOD = 10**9 + 7
        n = len(num)
        digits = [int(d) for d in num]
        total = sum(digits)
        if total % 2 != 0:
            return 0
        target = total // 2
        odd_len = (n + 1) // 2 # even_len == n // 2

        # Initialize DP table
        # dp[i][s] = set of (odds_counts, evens_counts, k) tuples
        # where k is the number of digits in odd positions
        dp = [[set() for _ in range(target + 1)] for _ in range(n + 1)]
        # Base case: empty string
        dp[0][0].add((tuple([0]*10), tuple([0]*10), 0))

        for i in range(n):
            for s in range(target + 1):
                for odds_counts, evens_counts, k in dp[i][s]:
                    # Try adding current digit to odds
                    if s + digits[i] <= target and k < odd_len:
                        new_odds = list(odds_counts)
                        new_odds[digits[i]] += 1
                        dp[i+1][s + digits[i]].add(
                          (tuple(new_odds), evens_counts, k + 1)
                        )
                    
                    # Try adding current digit to evens
                    if n - (i + 1) >= odd_len - k:  # Ensure we can still reach odd_len
                        new_evens = list(evens_counts)
                        new_evens[digits[i]] += 1
                        dp[i+1][s].add(
                          (odds_counts, tuple(new_evens), k)
                        )

        # Calculate total permutations
        total_perms = 0
        for odds_counts, evens_counts, k in dp[n][target]:
            if k == odd_len:  # Only count if we have the correct number of odd digits
                perms_odds = self.multinomial_coefficient(odds_counts)
                perms_evens = self.multinomial_coefficient(evens_counts)
                total_perms = (total_perms + perms_odds * perms_evens) % MOD

        return total_perms

    def countBalancedPermutationsDF(self, num: str) -> int:
        """Digit Frequency-based approach, bottom-up DP.
        For each digit value, for each possible way to assign its count to 
        odd/even positions, update the DP state incrementally. This uses a
        'rolling dp' pattern to create a new dp state for each digit 0-9, 
        starting with the previous dp.
        """

        MOD = 10**9 + 7
        n = len(num)
        digits = [int(d) for d in num]
        total = sum(digits)
        if total % 2 != 0:
            return 0
        target = total // 2
        odd_len = (n + 1) // 2

        # Count initial frequency of each digit in num
        digit_freq = [0] * 10
        for d in digits:
            digit_freq[d] += 1

        from collections import defaultdict
        # dp[(odd_sum, odd_count, odds_tuple, evens_tuple)] = 1 (set-like)
        # Start with empty assignment, ie no odds
        dp = { (0, 0, (0,)*10, (0,)*10): 1 }

        for d in range(10): # step through digits 0-9
            freq = digit_freq[d]
            if freq == 0:
                continue # this digit not present in num
            next_dp = defaultdict(int) # this will replace the current dp
            # For each way to split freq of digit d into k odds and freq-k evens
            for state in dp:
                odd_sum, odd_count, odds, evens = state
                for k in range( min(freq, odd_len - odd_count) + 1 ):
                    even_k = freq - k
                    if (n - odd_count) < even_k:
                        continue  # not enough slots left for evens
                    new_odd_sum = odd_sum + d * k
                    new_odd_count = odd_count + k
                    if new_odd_sum > target or new_odd_count > odd_len:
                        continue # overshot target or max # of odd numbers
                        
                    # otherwise, add new state
                    new_odds = list(odds)
                    new_evens = list(evens)
                    new_odds[d] += k
                    new_evens[d] += even_k
                    next_state = (
                        new_odd_sum, 
                        new_odd_count, 
                        tuple(new_odds), 
                        tuple(new_evens)
                    )
                    next_dp[next_state] = 1
            dp = next_dp

        total_perms = 0
        for (odd_sum, odd_count, odds, evens) in dp:
            if odd_sum == target and odd_count == odd_len:
                perms_odds = self.multinomial_coefficient(odds)
                perms_evens = self.multinomial_coefficient(evens)
                total_perms = (total_perms + perms_odds * perms_evens) % MOD
        return total_perms

    def countBalancedPermutationsReverseDP(self, num: str) -> int:
        """Reverse iteration DP approach to count balanced permutations.
        
        DP state: dp[sum][count] represents the number of ways to achieve a sum 
        of 'sum' with 'count' digits processed.
        Iterate backwards from target and even_len to build the DP state.
        """
        MOD = 10**9 + 7
        n = len(num)
        digits = [int(d) for d in num]
        total = sum(digits)
        if total % 2 != 0:
            return 0
        target = total // 2
        odd_len = (n+1) // 2
        even_len = n - odd_len

        # Initialize DP table
        dp = [[0] * (even_len + 1) for _ in range(target + 1)]
        dp[0][0] = 1  # Base case: no digits, zero sum

        counts = [0] * 10 # frequency of digits 0-9

        # Iterate backwards from target and even_len
        for d in digits:
            counts[d] += 1
            for sum_val in range(target, d-1, -1):
                for count in range(even_len, 0, -1):
                    prior_sum = sum_val - d
                    prior_cnt = count - 1
                    dp[sum_val][count] = (
                        dp[sum_val][count] + 
                        dp[prior_sum][prior_cnt]
                    ) % MOD

        # Calculate multinomial coefficient
        result = dp[target][even_len]
        result = (result * self.fact[odd_len]) % MOD
        result = (result * self.fact[even_len]) % MOD
        for cnt in counts:
            result = (result * self.inv_fact[cnt]) % MOD
        return result
    

    def countBalancedPermutations_sung_jinwoo(self, num):
        mod = 10**9+7
        n = len(num)
        total = sum(int(c) for c in num)
        if total % 2: return 0
        fact = [1]*(n+1)
        inv = [1]*(n+1)
        invFact = [1]*(n+1)
        for i in range(1,n+1): fact[i] = fact[i-1]*i % mod
        for i in range(2,n+1): inv[i] = mod - (mod//i)*inv[mod%i] % mod
        for i in range(1,n+1): invFact[i] = invFact[i-1]*inv[i] % mod
        halfSum = total//2
        halfLen = n//2
        dp = [[0]*(halfLen+1) for _ in range(halfSum+1)]
        dp[0][0] = 1
        digits = [0]*10
        for c in num:
            d = int(c)
            digits[d] += 1
            for i in range(halfSum, d-1, -1):
                for j in range(halfLen, 0, -1):
                    dp[i][j] = (dp[i][j] + dp[i-d][j-1]) % mod
        res = dp[halfSum][halfLen]
        print(f"dp[halfSum][halfLen]=")
        res = res * fact[halfLen] % mod * fact[n-halfLen] % mod
        for cnt in digits: res = res * invFact[cnt] % mod
        return res


"""
Testing Code

Each test is [(parameters to pass), expected]

"""
tests = [
    [["123"], 2],
    [["112"], 1],
    [["12"], 0],
    [["121"], 1],
    [["330"], 2],
    [["12345"], 0],
    [["123456"], 0],
    [["1234567"], 576],
    [["12345678"], 4608],
    [["1112345678"], 57600],
    [["123456789"], 0],
    [["6917368363"], 8000],
    [["1977522089"], 36000],
    [["0593136364172"], 19353600],
    [["482947768860194044298538"], 845579094],
    [["53246232578245872968259603958537"], 867933349],
    [["33593296415825621231886899510338994"], 919231388],
    [["46408223071894315077892189975338085"], 985956079],
    [["01234567890123456789012345678901234567890123456789012345678901234567890123456788"], 0],
    [["01234567890123456789012345678901234567890123456789012345678901234567890123456789"], 284226843],
]
from testing import runTests, timeTests
if __name__ == '__main__':
    runTests(Solution, tests)