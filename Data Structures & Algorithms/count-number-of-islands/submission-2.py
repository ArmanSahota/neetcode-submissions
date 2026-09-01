class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island = 0
        def dfs(R, C):
            if 0 > R or R >= ROWS or 0 > C or C >= COLS or grid[R][C] == "0":
                return 
            grid[R][C] = "0"
            dfs(R + 1, C)
            dfs(R - 1, C)
            dfs(R, C - 1)
            dfs(R, C + 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r,c)
        return island
       
