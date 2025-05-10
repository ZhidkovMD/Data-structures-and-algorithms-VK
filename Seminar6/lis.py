from typing import List


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lis = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        
        return max(lis)