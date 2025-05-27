"""

LeetCode Problem 222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes
Difficulty: Easy

Description:

Given a complete binary tree, count the number of nodes in the tree.

A complete binary tree is a tree where all levels, except possibly the
last, are filled and all nodes are as left as possible.

Brute force solution: Traverse the tree, counting nodes. Time: O(N)

Notes:
- Definition: In a Perfect tree, all leaf nodes are at the same level.
- In a perfect tree, given depth h, there are 2^h - 1 nodes and the last level
  has 2^(h - 1)
- Similarly, given n nodes, the height is log(n+1, 2)
- Another way of solving this is, how many nodes are in the last level
- Given that the last level will be filled from left to right, we can perform
  a binary search starting in the middle. When we find two differing depths,
  that is the transition. This last node is the number of nodes in the tree.

"""

from collections import deque
import bisect

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def depth_on_left(node):
            # traverse down left side, the maximum depth for a complete tree
            if not node:
                return 0
            return 1 + depth_on_left(node.left)
        
        def get_node(node, idx):
            """ Return node matching idx using a breadth-first search. """
            if not node or idx <= 1:
                return node
            parent = get_node(node, idx // 2) # even go left, odd go right
            if not parent:
                return parent
            elif (idx % 2) == 0:
                return parent.left
            else:
                return parent.right
        if not root:
            return 0
            
        depth = depth_on_left(root)
        right = (2 ** depth) -1 # for a perfect tree
        left = (right + 1) // 2 # least number of nodes at this depth
        
        # Helper method for bisect_left
        def is_node_missing(idx):
            return get_node(root, idx) is None
        
        # bisect_left returns first missing node, so last_present is one less
        last_present = (
            bisect.bisect_left(
                range(right + 1),
                True,
                lo=left,
                key=is_node_missing
            ) - 1
        )
        return last_present
    
    def count_nodes_manual(root: TreeNode) -> int:
        """ Pre-bisect, manual implementation of binary search. """
        def depth_on_left(node):
            # traverse down left side, the maximum depth for a complete tree
            if not node:
                return 0
            return 1 + depth_on_left(node.left)
        def depth_on_right(node):
            if not node:
                return 0
            return 1 + depth_on_right(node.right)
        
        def get_node(node, idx):
            """ Return node matching idx using a breadth-first search. """
            if not node or idx <= 1:
                return node
            parent = get_node(node, idx // 2) # even go left, odd go right
            if not parent:
                return parent
            elif (idx % 2) == 0:
                return parent.left
            else:
                return parent.right
        
        depth = depth_on_left(root)
        right = (2 ** depth) -1 # for a perfect tree
        left = (right + 1) // 2 # least number of nodes at this depth
        
        # check if perfect tree, binary search assumes get_node(right) == 
        if depth == depth_on_right(root):
            return right
        
        # binary search to find first real node between left and right
        mid = 0
        node = None
        while (right - left > 1):
            mid = left + ((right - left) // 2)
            node = get_node(root, mid)
            if node == None:
                right = mid
            else:
                left = mid
        
        return mid if node else left
    
    def count_nodes_leetcode(self, root: TreeNode) -> int:
        # shortest, cleanest code I saw on leetcode
        # Concept:
        # At each node, if the height of the right subtree is the height of the 
        # root -1, then the left subtree must be perfect and so will be (1<<h) - 1
        # + 1 (for the root) + the nodes in the right tree, aka (1<<h) + cnt(right)
        # if not, then the right tree is perfect and the left is not, so the nodes
        # are (1<<h-1) - 1 (for the reduced right sub tree) + 1 (root) + cnt(left)
        # or (1<<h-1) + cnt(left)
        def height(root):
            return -1 if not root else 1 + height(root.left)

        h = height(root)
        if h < 0:
            return 0
        elif height(root.right) == h - 1:
            return (1<<h) + count_nodes_leetcode(root.right)
        else:
        return (1<<h-1) + count_nodes_leetcode(root.left)


def makeTree(num_nodes: int) -> TreeNode:
    def next_val(val):
        return val + 1
    if num_nodes < 1:
        return None
    value = 1
    root = TreeNode(value)
    queue = deque([root])
    num_nodes -= 1
    while num_nodes > 0 and queue:
        node = queue.popleft()
        value = next_val(value)
        node.left = TreeNode(value)
        queue.append(node.left)
        num_nodes -= 1
        if num_nodes <= 0:
            return root
        value = next_val(value)
        node.right = TreeNode(value)
        queue.append(node.right)
        num_nodes -= 1
    return root

# Test cases
# Each test is [(parameters to pass), expected]
TEST_CASES = [
    [[makeTree(1)], 1],
    [[makeTree(2)], 2],
    [[makeTree(3)], 3],
    [[makeTree(4)], 4],
    [[makeTree(5)], 5],
    [[makeTree(6)], 6],
    [[makeTree(7)], 7],
    [[makeTree(8)], 8],
    [[makeTree(9)], 9],
    [[makeTree(10)], 10],
    [[makeTree(11)], 11],
    [[makeTree(12)], 12],
    [[makeTree(13)], 13],
    [[makeTree(14)], 14],
    [[makeTree(15)], 15],
]

if __name__ == '__main__':
    from testing import runTests
    runTests(Solution, TEST_CASES)
