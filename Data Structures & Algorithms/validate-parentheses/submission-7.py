class Solution:
    def isValid(self, s: str) -> bool:
        hashset = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for i in s:
            if i in hashset:
                if stack and stack[-1] == hashset[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
