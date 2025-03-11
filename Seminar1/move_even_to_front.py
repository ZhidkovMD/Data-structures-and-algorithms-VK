from typing import List


def move_even_to_front(nums: List[int]) -> None:
    even_ptr = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even_ptr], nums[i] = nums[i], nums[even_ptr]
            even_ptr += 1