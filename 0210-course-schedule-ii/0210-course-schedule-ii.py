class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for a, b in prerequisites:
            preMap[a].append(b)
        res = []
        visit = set()
        circle = set()
        def dfs(crs):
            if crs in visit:
                return True
            if crs in circle:
                return False
            circle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            circle.remove(crs)
            res.append(crs)
            visit.add(crs)
            return res
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
