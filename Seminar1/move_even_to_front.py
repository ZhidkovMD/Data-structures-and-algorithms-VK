from typing import List


def move_even_to_front(nums: List[int]) -> None:
    l = 0

    for r in range(len(nums)):
        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
