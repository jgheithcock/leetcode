# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

"""
Description:

Notes: Did research about array representation of a tree (see ../misc/tree_array.py)
Then saw that the input was a node...

Did in app, could use tree_array.py for testing.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.val}"
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node: return
            dfs(node.left)
            results.append(node.val)
            dfs(node.right)
        results = []
        dfs(root)
        return results

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[create_tree([1,None,2,3])], [1,3,2]],
    [[create_tree([1,2,3,4,5,None,8,None,None,6,7,9])], [4,2,6,5,7,1,3,9,8]],
    [[create_tree([])], []],
    [[create_tree([1])], [1]],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
