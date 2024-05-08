class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0

        def dfs(x, y):
            # Base condition to stop recursion if out of bounds or water or already visited
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 'L':
                return
            # Mark the land cell as visited by setting it to 'W'
            grid[x][y] = 'W'
            # Recursively visit all adjacent cells (up, down, left, right)
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                    dfs(i, j)
                    count += 1  # Increase the island count for each new starting point of DFS
        return count