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


