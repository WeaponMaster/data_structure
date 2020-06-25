from typing import List


def interpolationSearch(nums: List, val: int): #
    left = 0
    right = len(nums) - 1

    while left <= right:
        # 差值占总体的比例 换算成下标的
        mid = int((right - left)*(val - nums[left])/(nums[right] - nums[left]))
        if val < nums[mid]:
            left = mid
        elif val > nums[mid]:
            right = mid
        else:
            return mid

arr = list(range(30))
target = 10
print(interpolationSearch(arr,target))
