class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if r == ROWS or c == COLS or r < 0 or c < 0 or ((r, c)) in visit or (heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        res = []
        for R in range(ROWS):
            for C in range(COLS):
                if (R, C) in atl and (R, C) in pac:
                    res.append([R, C])
        return res 



        