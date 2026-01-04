class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        rows, cols = len(rooms), len(rooms[0])
        visit = set()

        def addrooms(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or rooms[r][c] == -1):
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
                addrooms(row, col + 1)
                addrooms(row, col - 1)
                addrooms(row + 1, col)
                addrooms(row - 1, col)
            dist += 1