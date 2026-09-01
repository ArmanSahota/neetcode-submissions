class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        Top = 0
        Bot = ROWS - 1
        while Top <= Bot:
            Mid = (Top + Bot) // 2
            if target > matrix[Mid][-1]:
                Top = Mid + 1
            elif target < matrix[Mid][0]:
                Bot = Mid - 1
            else: break

        
        L = 0
        R = COLS - 1
        while L <= R:
            M = (L + R) // 2
            if target > matrix[Mid][M]:
                L = M + 1
            elif target < matrix[Mid][M]:
                R = M - 1
            else:
                return True
        return False



        

        