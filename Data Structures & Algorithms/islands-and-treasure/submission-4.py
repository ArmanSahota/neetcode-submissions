class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        inf = 2147483647
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        steps = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if ROWS > nr >= 0 and COLS > nc >= 0 and grid[nr][nc] == inf:
                        grid[nr][nc] = steps + 1
                        q.append((nr, nc))
            steps += 1
        


        