class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        circle = set()
        visit = set()
        res = []
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
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
            