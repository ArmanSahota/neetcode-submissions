class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        q = deque()
        ROW = len(matrix) 
        COL = len(matrix[0]) 
        for R in range(ROW):
            for C in range(COL):
                if matrix[R][C] == 0:
                    q.append((R,C))
        while q:
            R, C = q.popleft()
            for i in range(ROW):
                matrix[i][C] = 0
            for i in range(COL):
                matrix[R][i] = 0
        

            


        
        