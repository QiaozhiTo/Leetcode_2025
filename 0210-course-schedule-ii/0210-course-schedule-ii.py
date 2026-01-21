class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit, cycle = set(), set()
        preMap = {i : [] for i in range(numCourses)}
        res = []
        for a, b in prerequisites:
            preMap[a].append(b)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        