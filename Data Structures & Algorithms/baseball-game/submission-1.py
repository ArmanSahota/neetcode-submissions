class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in operations:
            if i == "+":
                l = stack.pop()
                r = stack.pop()
                stack.append(r)
                stack.append(l)
                stack.append(l + r)
            elif i == "C":
                stack.pop()
            elif i == "D":
                l = stack.pop()
                stack.append(l)
                stack.append(l * 2)
            else:
                stack.append(int(i))
        for i in stack:
            res += i
        return res
            
        