'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        q = deque()
        visit = set()
        # no need for visit ? no you need visit
        def addrooms(r, c):
            if (r < 0 or r ==  rows or c < 0 or c == cols or rooms[r][c] == -1 or (r, c) in visit):
                return 
            q.append((r, c))
            visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    addrooms(r, c)
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = dist 
                addrooms(row + 1, col)
                addrooms(row - 1, col)
                addrooms(row, col + 1)
                addrooms(row, col - 1)
            dist += 1
        


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * cols for _ in range(rows)]
            visit[r][c] = True
            steps = 0
            while q :
                for _ in range(len(q)):
                    row, col = q.popleft()
                    # when get the gate, return steps
                    if rooms[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr in range(rows) and nc in range(cols) and rooms[nr][nc] != -1 and not visit[nr][nc]:
                            q.append((nr, nc))
                            visit[nr][nc] = True
                steps += 1
            return INF

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == INF:
                    rooms[r][c] = bfs(r, c)
        
                    
'''



class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))