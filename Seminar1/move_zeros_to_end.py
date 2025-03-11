from typing import List


def move_zeros_to_end(nums: List[int]) -> None:
    l = 0

    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1