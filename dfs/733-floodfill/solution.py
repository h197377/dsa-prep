
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or image[sr][sc] == color:
        return image
    
    n = len(image)
    m = len(image[0])
    
    def dfs(image, r, c, color, orig):
        if r < 0 or r >= n or c < 0 or c >= m or image[r][c] != orig:
            return 
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        image[r][c] = color
        for rr, cc in dirs:
            dfs(image, r + rr, c + cc, color, orig)

        return 

    dfs(image, sr, sc, color, image[sr][sc])
    
    return image
            