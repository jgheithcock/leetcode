'''
Leetcode problem 93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/description/
Difficulty: Medium

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You are not allowed to reorder or
remove any digits in s. You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]


Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]


Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

1 <= s.length <= 20
s consists of digits only.

'''

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        def octets(s, partial):
            if len(partial) == 4 and not s:
                ip = ".".join(partial)
                results.append(ip)
                return
            for i in range(1, min(3, len(s)) + 1):
                octet = s[:i]
                if int(octet) <= 255 and (octet[0] != '0' or len(octet) == 1):
                    octets(s[i:], partial + [octet])
                    
        octets(s,[])
        return results


TEST_CASES = [
    [["25525511135"],["255.255.11.135","255.255.111.35"]],
    [["0000"],["0.0.0.0"]],
    [["101023"],["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]]
]

# Testing Code
if __name__ == '__main__':
	from testing import runTests
	runTests(Solution, TEST_CASES)
