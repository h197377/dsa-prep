class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "1":
                return 
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            grid[i][j] = "0"
            for x, y in dirs:
                dfs(i + x, j + y)

            
        n = len(grid)
        m = len(grid[0])
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res