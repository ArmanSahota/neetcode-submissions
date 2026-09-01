class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            hashmap[course].append(pre)
        visit = set()
        def dfs(course):
            if hashmap[course] == []:
                return True
            if course in visit:
                return False
            
            visit.add(course)
            for pre in hashmap[course]:
                if dfs(pre) == False:
                    return False

            visit.remove(course)
            hashmap[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


            
