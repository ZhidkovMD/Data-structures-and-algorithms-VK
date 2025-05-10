from typing import List, Dict

class Solution:
    def has_cycle(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return False
            
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        
        def dfs(node: int, parent: int) -> bool:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        for node in range(n):
            if not visited[node]:
                if dfs(node, -1):
                    return True
        return False