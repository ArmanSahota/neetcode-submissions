class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions =[(0, 1), (1, 0), (-1, 0), (0, -1)]
        island = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                R, C = q.popleft()
                for dr, dc in directions:
                    nr, nc = R + dr, C + dc
                    if nr < ROWS and  nr >= 0 and nc < COLS and nc >= 0 and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"
                    else:
                        continue


        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == "1":
                    island += 1
                    bfs(R, C)
        return island


