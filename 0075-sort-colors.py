# 75. Sort Colors
# https://leetcode.com/problems/sort-colors

"""
Description: (Medium)

Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in the 
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and 
blue, respectively.

You must solve this problem without using the library's sort function.

Follow Up:

Could you come up with a one-pass algorithm using only constant extra space?


Intuition:
The key here is that this is an in-place sort without any library function.

See the editorial re https://en.wikipedia.org/wiki/Dutch_national_flag_problem

The thing I missed was that, when you get to a one, you just move on. Also key
is that you *don't* move on if you are at 2. Viz:

0|n|2: nums
0|0|4: [1, 2, 1, 0, 0]
0|1|4: [1, 2, 1, 0, 0] (no change to nums)
0|1|3: [1, 0, 1, 0, 2] (2 swapped with n[4], n now points to 0)
1|2|3: [0, 1, 1, 0, 2] (Note, never going to leave a 2 behind and zeros always
behind n0.)
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, n0, n2 = 0, 0, len(nums) - 1
        while n <= n2:
            if nums[n] == 0:
                nums[n], nums[n0] = nums[n0], nums[n]
                n0, n = n0 + 1, n + 1
            elif nums[n] == 2:
                nums[n], nums[n2] = nums[n2], nums[n]
                n2 -= 1
            else:
                n += 1

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[2,0,2,1,1,0]], [0,0,1,1,2,2]],
    [[[2,0,1]], [0,1,2]],
    [[[0,1]], [0,1]],
    [[[1,1,1,2,2,0,0]], [0,0,1,1,1,2,2]],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
