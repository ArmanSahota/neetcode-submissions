class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        connections = {i:[] for i in range(n)}
        for i, con in edges:
            connections[i].append(con)
            connections[con].append(i)
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for nei in connections[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n


