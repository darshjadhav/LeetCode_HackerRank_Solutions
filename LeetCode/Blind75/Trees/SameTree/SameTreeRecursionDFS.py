# LEETCODE 100: Recursive DFS to check if Trees are the Same Tree
# Time: O(p+q) = O(n)
# Space: BEST O(log(n)) WORST O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursion keeps going until both trees are null (meaning that there were not any unalike trees)
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
