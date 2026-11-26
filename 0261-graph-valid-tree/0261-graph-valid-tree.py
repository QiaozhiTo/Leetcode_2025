"""class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # adj is undirect, have to add par to compare with its children
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                # compare nei with node, not par
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n"""

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n

# definition of Tree: 1. all nodes are connected 2. no cycle
# all nodes are connected -- all nodes are visited, len(visit) == nodes#
# undirected edge, for kid node, need to pass the parent to avoid false cycle detection.
# for example for node 1, need to pass par 0 to avoid false cycle detection.