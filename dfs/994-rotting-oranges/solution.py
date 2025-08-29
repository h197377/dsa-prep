class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        good_oranges = 0
        q = deque()
        days = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    good_oranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if not good_oranges:
            return 0
        
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for d in dirs:
                    xx = x + d[0]
                    yy = y + d[1]
                    if xx >= 0 and xx < n and yy >= 0 and yy < m and grid[xx][yy] == 1:
                        good_oranges -= 1
                        grid[xx][yy] = 2
                        q.append((xx, yy))

            days += 1

        return days - 1 if good_oranges == 0 else -1

        