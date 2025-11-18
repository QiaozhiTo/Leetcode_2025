# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         # depth first search
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         area = 0

#         def dfs(r, c):
#             if (r < 0 or c < 0 or r >= rows or c >= cols 
#                 or (r,c) in visit or grid[r][c] == 0):
#                 # can't use continue here, why??
#                 return 0
#             visit.add((r,c)) 
#             return 1 + (dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) +dfs(r, c-1) )
#         for r in range(rows):
#             for c in range(cols):
#                 area = max(area, dfs(r,c))
#         return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # breadth first search     
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0   
        def dfs(r, c):
            q = deque()
            res = 0
            q.append((r,c))
            visit.add((r,c))
            while q:
                res += 1
                row, col = q.popleft()
                directions = [[0,1], [0,-1],[1,0], [-1,0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or c < 0 or r == rows or c == cols 
                        or (r,c) in visit or grid[r][c]== 0):
                        continue
                    q.append((r,c))
                    visit.add((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area, dfs(r,c))
        return area
