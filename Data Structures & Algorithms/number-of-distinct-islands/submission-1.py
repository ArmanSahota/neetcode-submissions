class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if (r, c) in seen or not grid[r][c]:
                return
            
            seen.add((r, c))
            current_island.add((r - r_origin, c - c_origin))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        seen = set()
        unique_island = set()
        for r in range(ROWS):
            for c in range(COLS):
                current_island = set()
                r_origin = r
                c_origin = c
                dfs(r, c) 
                if current_island:
                    unique_island.add(tuple(current_island))
        return len(unique_island)


        