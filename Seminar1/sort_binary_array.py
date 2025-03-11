from typing import List


def sort_binary_array(nums: List[int]) -> None:
    left, right = 0, len(nums) - 1

    while left < right:
        while left < right and nums[left] == 0:
            left += 1

        while left < right and nums[right] == 1:
            right -= 1

        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1