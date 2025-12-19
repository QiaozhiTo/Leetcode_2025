
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:return 0
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         islands = 0
#         def dfs(r, c):
#             q = collections.deque()
#             visit.add((r, c))
#             q.append((r, c))

#             while q:
#                 row, col = q.popleft()
#                 directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#                 for dr, dc in directions:
#                     r = row + dr
#                     c = col + dc
#                     if (r in range(rows) and c in range(cols) and
#                         grid[r][c] == '1' and (r,c) not in visit):
#                         visit.add((r, c))
#                         q.append((r,c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1' and (r, c) not in visit:
#                     dfs(r, c)
#                     islands += 1
#         return islands




# depth first search
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # islands = 0
        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
        #        return 
        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r,c)
        #             islands += 1
        # return islands


# breadth first search
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid: return 0
#         rows, cols = len(grid), len(grid[0])
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         islands = 0
#         visit = set()

#         def dfs(r,c):
#             q = deque()
#             q.append((r, c))
#             visit.add((r, c))
#             while q:
#                 r, c = q.popleft()
#                 for dr, dc in directions:
#                     r = dr + r
#                     c = dc + c
#                     if (r in range(rows) and c in range(cols) 
#                     and (r,c) not in visit and grid[r][c] == "1"):
#                         visit.add((r, c))
#                         q.append((r, c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r,c) not in visit:
#                     dfs(r,c)
#                     islands += 1
#         return islands

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:return 0
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         rows, cols = len(grid), len(grid[0])
#         island = 0 
#         visit = set()

#         def dfs(r, c):
#             q = deque([(r, c)])# q.append((r, c)) cause error
#             visit.add((r, c))
#             while q:
#                 row,col = q.popleft()
#                 for dr, dc in directions:
#                     nr, nc = row + dr, col+ dc
#                     if (nr in range(rows) and nc in range(cols) and 
#                         grid[nr][nc] == "1" and (nr, nc) not in visit):
#                         visit.add((nr, nc))
#                         q.append((nr, nc))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     dfs(r, c)
#                     island += 1
#         return island












class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visit.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
