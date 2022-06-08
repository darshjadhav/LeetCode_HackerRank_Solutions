# LEETCODE 104: BFS (LEVEL ORDER TRAVERSAL) for Max Depth of Binary Tree
# TIME: O(n)
# SPACE: O(n)
# Uses Queues

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        levelcount = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levelcount += 1

        return levelcount
