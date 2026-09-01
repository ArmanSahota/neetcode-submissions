class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window = {}
        countS1 = Counter(s1)
        have = 0
        need = len(countS1)
        L = 0
        for R in range(len(s1)):
            window[s2[R]] = 1 + window.get(s2[R], 0)
            if s2[R] in countS1 and window[s2[R]] == countS1[s2[R]]:
                have += 1
        
        if have == need:
            return True

        
        for R in range(len(s1), len(s2)):
            window[s2[R]] = 1 + window.get(s2[R], 0)
            window[s2[L]] -= 1 

            if s2[R] in countS1 and window[s2[R]] == countS1[s2[R]]:
                have += 1
            if s2[L] in countS1 and window[s2[L]] < countS1[s2[L]]:
                have -= 1
            if have == need:
                return True
            L += 1
        return False
            




            


        
        
            







        
        