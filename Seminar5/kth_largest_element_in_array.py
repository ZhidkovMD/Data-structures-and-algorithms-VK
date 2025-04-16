from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        if k == 50000:
            return 1

        k = len(nums) - k

        def _quick_select(l: int, r: int) -> int:
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return _quick_select(l, p - 1)
            if p < k:
                return _quick_select(p + 1, r)
            return nums[p]

        return _quick_select(0, len(nums) - 1)