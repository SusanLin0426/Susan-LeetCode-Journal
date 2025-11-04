from typing import List


def move_zeroes(nums: List[int]) -> None:
    """In-place moves zeros to the end while keeping order. O(n) time / O(1) space."""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
