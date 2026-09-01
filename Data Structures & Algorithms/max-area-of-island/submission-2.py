class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxLength = 0

        def dfs(r, c):
            nonlocal maxLength
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (1 + 
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1))
        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == 1:
                    maxLength = max(maxLength, dfs(R, C))
        return maxLength

