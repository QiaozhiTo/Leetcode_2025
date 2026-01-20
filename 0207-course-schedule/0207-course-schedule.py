class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        # preMap = collections.defaultdict(list)
        preMap = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[b].append(a)
        
        def dfs(crs):
            if crs in visit:
                return False
            # when visit a course without any prerequisite, return True directly
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            # when found crs has no cycle, cash preMap[crs] = []
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True