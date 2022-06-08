# LEETCODE 102: BFS Level Order Traversal for Binary Tree
# TIME: O(n)
# SPACE: O(n)
# https://leetcode.com/problems/binary-tree-level-order-traversal/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        while queue:
            qLen = len(queue)
            temp = []
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if temp:
                res.append(temp)

        return res
