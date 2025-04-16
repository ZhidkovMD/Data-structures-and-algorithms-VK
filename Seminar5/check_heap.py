from typing import Optional, List


class Solution:
    def is_heap(self, heap: List[int]) -> bool:
        if not heap:
            return True
        
        is_min_heap = True
        is_max_heap = True
        
        for i in range(len(heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < len(heap):
                if heap[i] > heap[left]:
                    is_min_heap = False
                if heap[i] < heap[left]:
                    is_max_heap = False
            
            if right < len(heap):
                if heap[i] > heap[right]:
                    is_min_heap = False
                if heap[i] < heap[right]:
                    is_max_heap = False
            
            if not is_min_heap and not is_max_heap:
                return False
        
        return is_min_heap or is_max_heap