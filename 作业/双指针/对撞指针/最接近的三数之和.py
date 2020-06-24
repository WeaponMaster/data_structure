"""
16 - 最接近的三数之和
问题描述
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2)

思路
这个题目跟 15 - 三数之和类似，只是需要保存一下最接近 target 的值，
搜索过程中碰到更接近的数就更新这个值。

具体步骤如下：

在数组 nums 中，进行遍历，每遍历一个值利用其下标 i，形成一个固定值 nums[i]。
使用前指针指向 left = i + 1 处，后指针指向 right = len(nums) - 1 处，
根据 sums = nums[i] + nums[left] + nums[right] 的结果，
判断 sums 与目标 target 的距离，如果更近则更新结果 a。
因为数组有序，如果 sums > target 则 right -= 1，
如果 sums < target 则 left += 1，如果 sums == target 则说明距离为 0，直接返回结果。
"""


from typing import List


def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2] - target)
    res = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        # 当前nums[i]情况下，搜索最接近的组合
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            # 比较sums与目标target的距离与之前最近的距离，如果更近则更新
            if abs(sums - target) < min:
                min = abs(sums - target)
                res = sums
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            # 如果sums == target，则说明距离为0，这就是最接近的数
            else:
                return sums
    return res

