# Floyd Warshall Algorithm
'''
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reach = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reach[u][v] = True
        for i in range(numCourses):
            for j in range(numCourses):
                if reach[j][i]: # j is prerequisite of i
                    for k in range(numCourses):
                        if reach[i][k]:# i is prerequistite of k
                            reach[j][k] = True # then j is reqrequisite of k
        return [reach[u][v] for u, v in queries]

### depth first search
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs].update(dfs(prereq))
                    # prereqMap[crs] = prereqMap[crs] | dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
'''
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:    
                    prereqMap[crs].update(dfs(pre))
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res