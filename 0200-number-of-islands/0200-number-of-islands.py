# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # bfs
#         rows, cols = len(grid), len(grid[0])
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         q = deque()
#         visit = set()
#         islands = 0

#         def bfs(r, c):
#             q.append([r, c])
#             visit.add((r, c))
#             while q:
#                 row, col = q.popleft()
#                 for dr, dc in directions:
#                     nr, nc = dr + row, dc + col
#                     if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in visit or grid[nr][nc] == '0':
#                         continue 
#                     visit.add((nr, nc))
#                     q.append([nr, nc])

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1' and (r, c) not in visit:
#                     bfs(r, c)
#                     islands += 1
#         return islands

# dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or grid[r][c] =='0':
                return
            visit.add((r, c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands

