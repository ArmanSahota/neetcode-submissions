class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True

            for n in adj[c]:
                if dfs(n) == True:
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c) == True:
                return ""
            
        return "".join(res[::-1])    