# 2999. Count the Number of Powerful Integers
# From: https://leetcode.com/problems/count-the-number-of-powerful-integers

"""
Description:
You are given three integers start, finish, and limit. You are also given a 
0-indexed string s representing a positive integer.

A positive integer x is called powerful if it ends with s (in other words, s is
a suffix of x) and each digit in x is at most limit.

Return the total number of powerful integers in the range [start..finish].

A string x is a suffix of a string y if and only if x is a substring of y that
starts from some index (including 0) in y and extends to the index 
y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.

tests = [ # test, expected
    # test = start, finish, limit, suffix
    [[1, 6000,4,"124"], 5], # 124, 1124, 2124, 3124, and, 4124,
                            # 5124 is in the range but 5 > limit
    [[15, 215, 6, "10"], 2] # 110, 210 - 310 is past the limit
    [[1000, 2000, 4, "3000"], 0] # 3000 is not between 1000 and 2000
]

Constraints:

- 1 <= start <= finish <= 10^15
- 1 <= limit <= 9
- 1 <= s.length <= floor(log10(finish)) + 1
- s only consists of numeric digits which are at most limit.
- s does not have leading zeros.


Intuition:

Start with suffix converted to int. Loop from 1-limit, then 1+(0-limit)
until you exceed finish. So the prefixes are effectively base-limit

"""
import math

class Solution:
    def numberOfPowerfulIntBrute(self, start: int, finish: int, limit: int, s: str) -> int:
        def numToBase(num, base):
            result = 0
            multiplier = 1
            while num > 0:
                remainder, num = num % base, num // base
                result += remainder * multiplier
                multiplier *= 10
            return result
        def numFromBase(num, base):
            result = 0
            while num > 0:
                result = (result * base) + (num % 10)
                num //= 10
            return result
            
        result = 0
        for ndx in range(finish):
            next_prefix = str(numToBase(ndx, limit + 1))
            candidate = int(next_prefix + s)
            if (candidate > finish):
                return result
            elif candidate >= start:
                print(candidate)
                result += 1
        return result
        
    def numberOfPowerfulIntBad(self, start: int, finish: int, limit: int, s: str) -> int:
        
        def maxInBase(num, limit):
            # return the largest number given a limit
            # e.g. for 123456789, base=4, return 123444444
            # for 987654321, limit=4, return 444444444
            # Step until num[ndx] > limit, num[ndx..len-1] = limit
            flip = False
            num_str = str(num)
            result = []
            limit = str(limit)
            for ndx in range(len(num_str)):
                flip = flip or (num_str[ndx] > limit)
                result.append(limit if flip else num_str[ndx])
            return int(''.join(result))
            
        def powerfulUnder(num, limit, suffix):
            digits_in_suffix = int(math.log(suffix, 10)) + 1
            num_prefix = num // (10 ** digits_in_suffix)
            # num_suffix = num % (10 ** digits_in_suffix)
            # print(f"{num=}: {num_prefix=} {num_suffix=}, {extra=}")
            max_in_base = maxInBase(num_prefix, limit)
            # Convert max_in_base from base (limit + 1) to base 10
            n_from_base = int(str(max_in_base), limit + 1)
            # print(f"{num=}: {nFromBase=}, returning {nFromBase + extra}")
            # Add 1 if the suffix itself is in range
            return nFromBase + (1 if num >= suffix else 0)
            
        suffix = int(s)
        pFinish = powerfulUnder(finish, limit, suffix)
        pStart = powerfulUnder(start, limit, suffix)
        #print(f"{pFinish=}, {pStart=}")
        return pFinish - pStart
        
    def numberOfPowerfulIntAI(self, start: int, finish: int, limit: int, s: str) -> int:
        def powerfulUnder(num, limit, suffix):
            """Count the number of powerful integers ≤ num.
            
            A powerful integer ends with suffix and has all digits ≤ limit.
            
            Args:
                num: The upper bound
                limit: Maximum allowed digit value
                suffix: The required suffix
            """
            # First check if suffix itself is valid
            if not all(int(d) <= limit for d in str(suffix)):
                return 0
                
            # If num equals suffix, return 1 if it's valid
            if num == suffix:
                return 1
                
            if num < suffix:
                return 0
                
            count = 1  # Count suffix itself
            
            # Now try all possible prefixes
            digits_in_suffix = len(str(suffix))
            max_prefix = num // (10 ** digits_in_suffix)
            
            # For each length of prefix
            max_prefix_len = len(str(max_prefix))
            for length in range(1, max_prefix_len + 1):
                # For each possible first digit
                max_first = min(limit, int(str(max_prefix)[0]) if length == max_prefix_len else limit)
                for first in range(1, max_first + 1):
                    # For remaining positions, we can use any digit up to limit
                    remaining = length - 1
                    if length == max_prefix_len:
                        # Need to check against max_prefix
                        prefix_start = int(str(first) + "0" * remaining)
                        prefix_end = prefix_start + (10 ** remaining) - 1
                        if prefix_end > max_prefix:
                            prefix_end = max_prefix
                        # Count valid prefixes in this range
                        for prefix in range(prefix_start, prefix_end + 1):
                            if all(int(d) <= limit for d in str(prefix)):
                                full_num = prefix * (10 ** digits_in_suffix) + suffix
                                if full_num <= num:
                                    count += 1
                    else:
                        # All combinations of remaining digits up to limit are valid
                        count += (limit + 1) ** remaining
                    
            return count
        
        suffix = int(s)
        return powerfulUnder(finish, limit, suffix) - powerfulUnder(start, limit, suffix)
    
    def numberOfPowerfulIntA12(self, start: int, finish: int, limit: int, s: str) -> int:
        # This was the next solution - the AI wrote this from scratch seemingly but it is way off
        def powerfulUnder(num: int, limit: int, suffix: int) -> int:
            """Count the number of powerful integers ≤ num.
            
            A powerful integer ends with suffix and has all digits ≤ limit.
            
            Args:
                num: The upper bound
                limit: Maximum allowed digit value
                suffix: The required suffix
            """
            # First check if suffix itself is valid
            if not all(int(d) <= limit for d in str(suffix)):
                return 0
                
            # If num equals suffix, return 1 if it's valid
            if num == suffix:
                return 1
                
            if num < suffix:
                return 0
                
            # Count suffix itself
            count = 1
            
            # Get the prefix part of num
            digits_in_suffix = len(str(suffix))
            max_prefix = num // (10 ** digits_in_suffix)
            
            if max_prefix == 0:
                return count
                
            # Convert max_prefix to base (limit + 1)
            # This gives us the count of all valid prefixes
            max_prefix_str = str(max_prefix)
            max_prefix_len = len(max_prefix_str)
            
            # Count all prefixes shorter than max_prefix_len
            for length in range(1, max_prefix_len):
                count += (limit + 1) ** length
                
            # Count prefixes of max_prefix_len
            for i, digit in enumerate(max_prefix_str):
                digit = int(digit)
                if digit > limit:
                    digit = limit
                remaining = max_prefix_len - i - 1
                count += digit * (limit + 1) ** remaining
                if digit < int(max_prefix_str[i]):
                    # If we've found a digit less than the corresponding digit in max_prefix,
                    # all remaining digits can be any value up to limit
                    count += (limit + 1) ** remaining
                    break
                    
            return count
            
        suffix = int(s)
        pFinish = powerfulUnder(finish, limit, suffix)
        pStart = powerfulUnder(start, limit, suffix)
        return pFinish - pStart

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def powerfulUnder(num: int, limit: int, suffix: int) -> int:
            """Count the number of powerful integers ≤ num.
            
            A powerful integer ends with suffix and has all digits ≤ limit.
            
            Args:
                num: The upper bound
                limit: Maximum allowed digit value
                suffix: The required suffix
            """
            # First check if suffix itself is valid
            if not all(int(d) <= limit for d in str(suffix)):
                return 0
                
            # If num equals suffix, return 1 if it's valid
            if num == suffix:
                return 1
                
            if num < suffix:
                return 0
                
            # Convert num to string for digit-by-digit processing
            num_str = str(num)
            suffix_str = str(suffix)
            suffix_len = len(suffix_str)
            
            # If num is shorter than suffix, no valid numbers
            if len(num_str) < suffix_len:
                return 0
                
            # DP table: dp[i][tight] = count of valid numbers up to position i
            # where tight means we're still matching the prefix of num exactly
            dp = {}
            
            def count(i: int, tight: bool) -> int:
                if (i, tight) in dp:
                    return dp[(i, tight)]
                    
                # Base case: we've processed all digits
                if i == len(num_str):
                    return 1
                    
                # If we're in the suffix part, we must match the suffix
                if i >= len(num_str) - suffix_len:
                    suffix_pos = i - (len(num_str) - suffix_len)
                    required_digit = int(suffix_str[suffix_pos])
                    
                    if tight:
                        # Must match num's digit exactly
                        if int(num_str[i]) < required_digit:
                            return 0
                        if int(num_str[i]) > required_digit:
                            return count(i + 1, False)
                        return count(i + 1, True)
                    else:
                        # Can use any digit up to limit
                        if required_digit > limit:
                            return 0
                        return count(i + 1, False)
                        
                # We're in the prefix part
                if tight:
                    max_digit = int(num_str[i])
                    if max_digit > limit:
                        max_digit = limit
                    result = 0
                    for d in range(0, max_digit + 1):
                        if d < int(num_str[i]):
                            result += count(i + 1, False)
                        else:
                            result += count(i + 1, True)
                    dp[(i, tight)] = result
                    return result
                else:
                    # Can use any digit up to limit
                    result = (limit + 1) * count(i + 1, False)
                    dp[(i, tight)] = result
                    return result
                    
            return count(0, True)
        
        suffix = int(s)
        pFinish = powerfulUnder(finish, limit, suffix)
        pStart = powerfulUnder(start - 1, limit, suffix)
        return pFinish - pStart
        

# Each test is [(parameters to pass), expected]

TEST_CASES = [
    [[1, 6000, 4, "124"], 5],  # 124, 1124, 2124, 3124, and 4124
    [[15, 215, 6, "10"], 2],   # 110, 210
    [[20, 1159, 5, "20"], 8],
    [[1000, 2000, 4, "3000"], 0], # 3000 is not between 1000 and 2000
    [[98, 1335899, 9, "99"], 13358 + 1], # +1 if start < suffix
    [[100, 1335899, 9, "99"], 13358], # +1 if start < suffix
    [[1114, 1864854501, 7, "27"], 4194295],
    [[0, 333, 3, '3'], 15 + 1], # max - suffix = 33, numFromBase(33, 4) = 15

    [[1114, 1234854501, 7, "27"], 2740215], # last = 1234777727

    [[1114, 1234854544, 7, "27"], 2740215], # last (same) = 1234777727
    [[10, 2215, 4, '12'], 13],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
