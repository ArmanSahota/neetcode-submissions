from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        res = []

        for course, pre in prerequisites:
            hashmap[course].append(pre)

        visit = set()
        done = set()

        def dfs(course):
            if course in visit:
                return False
            if course in done:
                return True

            visit.add(course)

            for pre in hashmap[course]:
                if not dfs(pre):
                    return False

            visit.remove(course)
            done.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res