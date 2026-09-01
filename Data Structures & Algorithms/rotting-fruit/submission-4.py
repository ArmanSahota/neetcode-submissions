class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        visit = set()
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if ROWS > nr >= 0 and COLS > nc >= 0 and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        visit.add((nr, nc))
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1
        


