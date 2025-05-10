from collections import deque
from typing import List

class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
            
        color = [0] * len(graph)
        
        def bfs(start: int) -> bool:
            if color[start] != 0:
                return True
                
            queue = deque([start])
            color[start] = -1
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
            return True
        
        for node in range(len(graph)):
            if not bfs(node):
                return False
        return True