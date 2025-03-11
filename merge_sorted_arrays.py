from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Last index of nums1
    last = n + m - 1

    # Merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # If there are remaining elements in nums2, copy them
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1