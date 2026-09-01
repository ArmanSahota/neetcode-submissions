class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()

        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == 0:
                    q.append((R, C))
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0 and grid[nr][nc] == INF:
                        grid[nr][nc] = steps + 1
                        q.append((nr, nc))
                
            steps += 1
        