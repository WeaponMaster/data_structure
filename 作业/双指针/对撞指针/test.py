from typing import List

def threeSum(nums: List[int]) -> List:
    nums.sort()
    res = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        left = i+1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))