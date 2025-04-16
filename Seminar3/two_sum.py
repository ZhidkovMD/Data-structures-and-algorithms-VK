from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in num_dict:
            return [num_dict[difference], index]
        num_dict[number] = index
    return None