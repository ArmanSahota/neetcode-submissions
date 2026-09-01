class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0

        def dfs(R, C):
            if R == rows or C == cols or R < 0 or C < 0 or grid[R][C] == "0":
                return 
            grid[R][C] = "0"
            dfs(R + 1, C)
            dfs(R - 1, C)
            dfs(R, C + 1)
            dfs(R, C - 1) 
        
        for R in range(rows):
            for C in range(cols):
                if grid[R][C] == "1":
                    island += 1
                    dfs(R, C)
        return island