class Solution:
    def isValid(self, s: str) -> bool:
        open_p = []
        closed_p = {")" : "(", "}" : "{", "]" : "["}

        for p in s:
            if open_p and p in closed_p:
                if open_p[-1] == closed_p[p]:
                    open_p.pop()
                else:
                    return False
            else:
                open_p.append(p)
        return False if open_p else True
