class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 /values[i]])
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q = deque([(src, 1)])
            visit = set()
            visit.add(src)
            
            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei, w * weight])
            return -1
        return [bfs(q[0], q[1]) for q in queries]
