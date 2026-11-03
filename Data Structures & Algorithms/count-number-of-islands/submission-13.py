class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [1,0], [-1, 0], [0, -1]]
        islands = 0
        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                grid[r][c] = '0'

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0 and grid[nr][nc] == "1":
                        q.append([nr, nc])
                        grid[nr][nc] = '0'
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        return islands
                

