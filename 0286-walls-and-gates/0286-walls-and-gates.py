class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addroom(r, c):
            if (r in range(rows) and c in range(cols) and (r, c) not in visit and rooms[r][c] != -1):
                q.append((r, c))
                visit.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = dist
                addroom(row, col + 1)
                addroom(row, col - 1)
                addroom(row + 1, col)
                addroom(row - 1, col)
            dist += 1

