class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        inf = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(R, C):
            q = deque([(r, c)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[R][C] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return inf 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == inf:
                    grid[r][c] = bfs(r, c)

