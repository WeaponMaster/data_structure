from typing import List

def reverse(nums: List[int]):
    left = 0
    right = len(nums)-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    return nums


if __name__ == '__main__':
    l = list(range(10))
    print(reverse(l))