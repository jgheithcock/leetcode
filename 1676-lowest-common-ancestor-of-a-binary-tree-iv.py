#!/usr/bin/env python3

# 1123: Lowest Common Ancestor of Deepest Leaves
# From Leetcode daily challenge
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
# Also see: 1676. Lowest Common Ancestor of a Binary Tree IV
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            if left_depth > right_depth:
                return (left_depth+1, left_subtree)
            elif right_depth > left_depth:
                return (right_depth+1, right_subtree)
            else:
                return (left_depth+1, node)
        return dfs(root)[1]