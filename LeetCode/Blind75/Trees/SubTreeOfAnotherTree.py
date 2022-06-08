# LEETCODE 572: Recursive DFS For Subtree of another Tree
# Time: O(root*subRoot) -> O(n)
# Space: BEST O(logn) WORST O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If empty then it will be a subtree (Base Case)
        if not subRoot:
            return True
        # If there is no tree when subtree is not empty (due to previous case)
        if not root:
            return False
        # Check if they are the same trees
        if self.sameTree(root, subRoot):
            return True

        # If not same subtree, then go to next node (DFS)
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def sameTree(self, root, subRoot):
        # Base Case 1
        if not root and not subRoot:
            return True
        # Base Case 2: If both exist and if both values are equal to each other
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

        return False
