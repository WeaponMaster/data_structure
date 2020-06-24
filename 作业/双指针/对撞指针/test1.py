from typing import List

def threeSumClosest(nums: List[int], target: int)->int:
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2] - target)
    res = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums)-1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if abs(sum - target) < min:
                min = abs(sum - target)
                res = sum
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return sum
    return res
l = [-1,2,1,-4]
print(threeSumClosest(l,1))
