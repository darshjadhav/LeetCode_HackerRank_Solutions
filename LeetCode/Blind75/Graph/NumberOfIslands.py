# LEETCODE 200: Number of Islands in Grid using BFS Traversal
# TIME: O(m*n) (O(row*col))
# SPACE: O(min(m,n)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(m,n).
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(i, j):
            queue = deque() # Create Queue
            visited.add((i,j)) # Add grid location to visited set
            queue.append((i,j)) # Add grid location to queue

            while queue:
                row, col = queue.popleft() # Pop grid loc from queue (Change this to .pop() for DFS (making it a stack))
                directions = [[0,1], [1,0], [0,-1], [-1,0]] # Take all 4 directions we can move
                for dr, dc in directions:
                    i, j = row + dr, col + dc # Add each direction to current grid loc
                    if (i in range(rows) and # Check if new loc is in bounds of rows
                        j in range(cols) and # Check if new loc is in bounds of cols
                        grid[i][j] == "1" and # Check if new loc in grid == "1"
                        (i,j) not in visited): # Check if new loc has not been visited before
                        queue.append((i, j)) # Append new loc to queue
                        visited.add((i,j)) # Add new loc to visited set

        # Go through each value in grid
        for i in range(rows):
            for j in range(cols):
                # Check if grid val is island and we haven't visited it
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j) # Conduct BFS
                    islands += 1 # Add Island since we haven't visited via BFS (which checks for adjacents)

        return islands
