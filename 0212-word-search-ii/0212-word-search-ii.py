class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)

        rows, cols = len(board), len(board[0])
        res, visit= set(), set()
               
        def dfs(r, c, node, path):
            if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            (r, c) in visit or 
            board[r][c] not in node.children):
                return 

            visit.add((r,c))
            node = node.children[board[r][c]]
            path += board[r][c]
            if node.end:
                res.add(path)
            
            dfs(r, c+1, node, path)
            dfs(r, c-1, node, path)
            dfs(r+1, c, node, path)
            dfs(r-1, c, node, path)

            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
        