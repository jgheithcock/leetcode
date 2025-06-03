"""
LeetCode Problem 12: Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.
Constraints: 1 <= num <= 3999
"""

from typing import List, Tuple

# Roman numeral mapping from decimal to roman
DECIMAL_TO_ROMAN = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.

        Args:
            num: An integer between 1 and 3999

        Returns:
            The Roman numeral representation as a string
        """
        roman_parts: List[str] = []
        num_str = str(num)[::-1]

        for position in range(len(num_str) - 1, -1, -1):
            place_value = 10**position
            digit = int(num_str[position])

            if digit * place_value in DECIMAL_TO_ROMAN:
                roman_parts.append(DECIMAL_TO_ROMAN[digit * place_value])
            else:
                if digit >= 5:
                    roman_parts.append(DECIMAL_TO_ROMAN[5 * place_value])
                    digit -= 5
                roman_parts.extend([DECIMAL_TO_ROMAN[1 * place_value]] * digit)

        return "".join(roman_parts)

    def intToRomanShort(self, num: int) -> str:
        """
        A more concise implementation to convert an integer to a Roman numeral.

        Args:
            num: An integer between 1 and 3999

        Returns:
            The Roman numeral representation as a string
        """
        roman_values: List[Tuple[int, str]] = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""
        for value, symbol in roman_values:
            while num >= value:
                result += symbol
                num -= value
        return result


# Test Code
# Each test is [(parameters to pass), expected]

TEST_CASES = [
    [[3749], "MMMDCCXLIX"],
    [[58], "LVIII"],
    [[1994], "MCMXCIV"],
]

if __name__ == "__main__":
    from testing import runTests

    runTests(Solution, TEST_CASES)
