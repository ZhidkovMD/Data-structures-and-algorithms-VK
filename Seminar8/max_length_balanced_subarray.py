from typing import List, Dict

class Solution:
    def find_max_length(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        count_map: Dict[int, int] = {0: -1}
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            
            if count in count_map:
                max_len = max(max_len, i - count_map[count])
            else:
                count_map[count] = i
                
        return max_len