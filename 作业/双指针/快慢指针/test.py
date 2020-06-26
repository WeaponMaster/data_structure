from typing import List,Tuple


class Solution:

    def removeElement(self, nums: List, val: int):
        slow = 0
        fast = 0
        # [0,1,2,2,3,0,4,2]
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1  # 慢指针前进的前提是快指针发现了不同值
                fast += 1
            else:
                fast += 1
        return slow

class Solution1:

    def towSum(self,nums: List, target: int):
        left = 0
        right = len(nums)-1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
                print(nums[left],nums[right])
                left += 1
                right -= 1
            else:
                if curr < target:
                    left += 1
                else:
                    right -= 1

