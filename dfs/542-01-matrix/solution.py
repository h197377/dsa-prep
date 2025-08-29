class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        res = [[-1 for _ in range(m)] for _ in range(n)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([])

        for i in range(n):
            for j in range(m):
                if res[i][j] == -1 and mat[i][j] == 0:
                    q.append( ((i,j), 0) )
                    res[i][j] = 0

        while q:
            coor, dist = q.popleft()
            x, y = coor
            for d in dirs:
                xx = x + d[0]
                yy = y + d[1]

                if xx >= 0 and xx < n and yy >= 0 and yy < m and res[xx][yy] == -1:
                    res[xx][yy] = dist + 1
                    q.append( ((xx, yy), dist + 1) )

        return res
