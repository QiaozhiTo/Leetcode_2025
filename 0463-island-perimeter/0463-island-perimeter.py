class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0
            visit.add((r, c))
            perime = dfs(r, c +1) + dfs(r, c-1) + dfs(r + 1, c) + dfs(r - 1, c)
            return perime
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return 0