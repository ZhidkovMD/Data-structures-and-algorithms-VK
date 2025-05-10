from typing import List

class Solution:
    def maximum_subarray_sum(self, nums: List[int], k: int) -> int:
        if k <= 0 or k > len(nums):
            return 0
            
        max_sum = current_sum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
            
        return max_sum