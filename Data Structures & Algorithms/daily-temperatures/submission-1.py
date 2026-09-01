class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for R in range(len(temperatures) - 1):
            L = R + 1 
            while L < len(temperatures):
                if temperatures[R] < temperatures[L]:
                    res.append(L - R)
                    break
                L += 1
            if L == len(temperatures):
                res.append(0)
        res.append(0)
        return res
                

