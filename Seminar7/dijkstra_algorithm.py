import heapq
from typing import List, Dict, Tuple

class Solution:
    def dijkstra(self, n: int, edges: List[List[Tuple[int, int]]], start: int) -> Dict[int, int]:
        distances = {node: float('inf') for node in range(n)}
        distances[start] = 0
        
        heap = [(0, start)]
        
        while heap:
            current_dist, u = heapq.heappop(heap)
            
            if current_dist > distances[u]:
                continue
                
            for (v, weight) in edges[u]:
                distance = current_dist + weight
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(heap, (distance, v))
        
        return distances