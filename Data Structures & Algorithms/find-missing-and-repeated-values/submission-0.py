class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid)):
                count[grid[i][j]] += 1

        double = missing = 0

        for num in range(1, len(grid) * len(grid) + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num

        return [double, missing]