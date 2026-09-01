class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        con = {i:[] for i in range(n)}
        visit = [False] * n

        for u, v in edges:
            con[u].append(v)
            con[v].append(u)
        print(con)

        def dfs(node):
            for nei in con[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0


        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
        


        