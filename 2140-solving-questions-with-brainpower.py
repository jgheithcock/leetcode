# 2140. Solving Questions With Brainpower
# From: https://leetcode.com/problems/solving-questions-with-brainpower

"""
You are given a 0-indexed 2D integer array questions where questions[i] = 
[pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the
questions in order (i.e., starting from question 0) and make a decision whether
to solve or skip each question. Solving question i will earn you pointsi points
but you will be unable to solve each of the next brainpower i questions. If you
skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve
questions 1 and 2.

If instead, question 0 is skipped and question 1 is solved, you will earn 4
points but you will be unable to solve questions 2 and 3.

Return the maximum points you can earn for the exam.

Constraints:
- 1 <= questions.length <= 105
- questions[i].length == 2
- 1 <= pointsi, brainpoweri <= 105

Intuition:

Based on the "maximum points" and the similarity to the knapsack problem, this
seems like a dynamic programming problem. However, the large size makes me look
at a greedy algorithm. This turned out to be wildly sub-optimal.

For the dynamic programming version, dp will hold the max for solving that nth
question. We fill by going backward and incrementing the nth question with
either the points for nth plus the points for the next we can get to (which
will already have been filled in) or the points for the nth+1 (aka skipping),
whichever is the maximum. For the case where next question takes us out of
bounds, just look at the points of this question vs the next one. To handle
checking the next one when we are on the last, add an extra element to dp for
length + 1. 
"""

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        return self.mostPointsDP(questions)
    
    def mostPointsGreedy(self, questions: List[List[int]]) -> int:
        max_points = 0
        ndx = 0
        while ndx <= (len(questions) - 1):
            points1, brainpower1 = questions[ndx]
            if points1 > 0:
                max_points += points1
                ndx += brainpower1 + 1
        return max_points
    
    def mostPointsDP(self, questions: List[List[int]]) -> int:
        num = len(questions)
        dp = [0] * (num + 1)
        best = [-1] * (num + 1) # -1 to skip
        
        for ndx in range(num - 1, -1, -1):
            points, brainpower = questions[ndx]
            next_q = ndx + 1 + brainpower
            next_points = dp[next_q] if next_q < num else 0
            take_points = points + next_points
            skip_points = dp[ndx + 1]
            if take_points > skip_points:
                dp[ndx] = take_points
                best[ndx] = next_q
            else: # best is to skip
                dp[ndx] = max(take_points, skip_points)
        return dp[0]
    
    def mostPointsBest(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n-1] = questions[n-1][0]

        for i in range(n-2, -1 , -1):
            p, s = questions[i][0], questions[i][1] + i + 1
            if s >= n:
                dp[i] = max(p, dp[i+1])
            else:
                dp[i] = max(p+dp[s], dp[i+1])
        return dp[0]
    
def reconstructBest(best: list[int], questions: list[list[int]]) -> list[int]:
    ndx, num = 0, len(questions)
    solution = []
    while ndx < num:
        if best[ndx] > 0:
            solution.append(questions[ndx][0])
            ndx = best[ndx]
        else:
            ndx += 1
    return solution

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[[ [3,2],[4,3],[4,4],[2,5] ]], 5],
    [[[ [1,1],[2,2],[3,3],[4,4],[5,5] ]], 7],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
