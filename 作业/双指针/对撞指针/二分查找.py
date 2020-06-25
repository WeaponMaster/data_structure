from typing import List
import sys


def binarySearch(nums: List, val: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if val == nums[left]:
            return left
        elif val == nums[right]:
            return right
        else:
            mid = (left + right)//2
            if val < nums[mid]:
                left = mid
            elif val > nums[mid]:
                right = mid
            else:
                return mid


def binarySearch2(nums: List, val: int):
    left = -1
    right = len(nums)
    while left <= right:
        mid = (left + right)//2
        if val < nums[mid]:
            left = mid
        elif val > nums[mid]:
            right = mid
        else:
            return mid


def binarySearch3(nums: List, val: int): #
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left)//2  # 适用于其他编程语言
        if val < nums[mid]:
            left = mid
        elif val > nums[mid]:
            right = mid
        else:
            return mid
# 递归版

def binarySearch4(nums: List, val: int,left: int, right: int):
    if right > 0:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            return binarySearch4(nums, val, left, mid-1)
        else:
            return binarySearch4(nums,val,mid+1,right)
    else:
        return -1

arr = list(range(30))
target = 10
print(binarySearch4(arr,target,0,len(arr)))