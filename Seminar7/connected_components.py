from typing import List

class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        components = 0
        
        def dfs(node):
            stack = [node]
            visited[node] = True
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        for node in range(n):
            if not visited[node]:
                dfs(node)
                components += 1
                
        return components