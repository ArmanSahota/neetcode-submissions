class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.string = s

        if not k:
            return self.is_p(0, len(s) - 1)

        memo = {} 

        def helper(L, R, k):
            if (L, R, k) in memo:
                return memo[(L, R, k)]
            elif not k:
                memo[(L, R, k)] = self.is_p(L, R)
            else:
                while L < R:
                    if self.string[L] != self.string[R]:
                        memo[(L, R, k)] = helper(L + 1, R, k - 1) or helper(L, R - 1, k - 1)

                        return memo[(L, R, k)]
                    L += 1
                    R -= 1
                memo[(L, R, k)] = True
            return memo[(L, R, k)]
        return helper(0, len(self.string) - 1, k)
        
    def is_p(self, L, R):
        while L < R:
            if self.string[L] != self.string[R]:
                return False
            L += 1
            R -= 1
        return True
