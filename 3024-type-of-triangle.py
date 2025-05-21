# 3024. Type of Triangle
# https://leetcode.com/problems/type-of-triangle

from typing import List
from statistics import median

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (
            nums[0] + nums[1] <= nums[2]
            or nums[0] + nums[2] <= nums[1]
            or nums[1] + nums[2] <= nums[0]
        ):
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

    # MikPosp's wonderful 1-liner:
    def triangleTypeMikPosp(self, a: List[int]) -> str:
        return ('none','equilateral','isosceles','scalene')[(max(a)<min(a)+median(a))*len({*a})]

    # Broken down:
    def triangleTypeMikPospLong(self, a: List[int]) -> str:
        # Triangle is only valid if the two shorter sides are > longest
        valid = (max(a)<min(a)+median(a)) # No need to sort
        num_unique_sides = len({*a})
        # {*a} creates a set of only unique numbers, so len() is 1, 2, or 3
        # Thus, valid * num_unique_sides is 0 (if !valid), or 1, 2, 3
        return ('none','equilateral','isosceles','scalene')[valid * num_unique_sides]

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[3,3,3]], "equilateral"],  # All sides equal
    [[[3,4,5]], "scalene"],  # All sides different
    [[[3,3,4]], "isosceles"],  # Two sides equal
    [[[1,2,3]], "none"],  # Not a valid triangle
    [[[2,2,3]], "isosceles"],  # Two sides equal
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)