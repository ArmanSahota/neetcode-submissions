class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for l in range(cols):
                if matrix[i][l] == target:
                    return True
        return False

        