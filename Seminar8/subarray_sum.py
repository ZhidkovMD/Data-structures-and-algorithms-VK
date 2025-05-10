from typing import List, Dict

class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums: Dict[int, int] = {0: 1}

        for num in nums:
            current_sum += num
            count += prefix_sums.get(current_sum - k, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count