# LEETCODE 133: Clone Graph using DFS
# TIME: O(n+m)
# SPACE: O(n)
# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        newGraph = {}

        def dfs(node):
            if node in newGraph:
                return newGraph[node]

            copyNode = Node(node.val)
            newGraph[node] = copyNode

            for elem in node.neighbors:
                 copyNode.neighbors.append(dfs(elem))
            return copyNode


        return dfs(node) if node else None
