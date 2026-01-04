class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        for a, b in prerequisites:
            preMap[a].append(b)
        visiting = set()
        def dfs(crs):  
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)     
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True        