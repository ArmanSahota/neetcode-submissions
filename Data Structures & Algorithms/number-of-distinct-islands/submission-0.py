class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(row, col, direction):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            path_sig.append(direction)
            dfs(row + 1, col, "D")
            dfs(row - 1, col, "U")
            dfs(row, col + 1, "R")
            dfs(row, col - 1, "L")
            path_sig.append("0")
        seen = set()
        unique_island = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path_sig = []
                dfs(row, col, "0")
                if path_sig:
                    unique_island.add(tuple(path_sig))
        return len(unique_island)