# LEETCODE 226: Invert Binary Tree using Iteration (Breadth First Search)
# TIME: O(n)
# SPACE: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = collections.deque([root])

        while queue:
            curr = queue.popleft()

            if curr is None:
                continue

            curr.left, curr.right = curr.right, curr.left

            queue.append(curr.left)
            queue.append(curr.right)

        return root
