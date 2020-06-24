"""
1 - 两数之和
题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9，所以返回 [0, 1]

思路
我们马上可以想到一个暴力解法：遍历每个元素 x，并查找是否存在一个值与 target - x 相等的目标元素。但是这个方法时间复杂度达到 O(n^2)。

因此，我想到用哈希表以空间换取速度，将查找时间从 O (n) 降低到 O (1)。

在进行迭代并将元素插入到哈希表的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。如果它存在，那我们已经找到了对应解，并立即将其返回。

注意：这里没有使用对撞指针，因为这里数组是无序的，而排序的时间复杂度为 O (nlogn)，所以不太划算。

"""
from typing import List

def two_sum(nums: List[int], target: int):
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i]+j == target:
                return True
    return False

l = [1,2,4,7,11,15]
print(two_sum(l,15))

# [1,  2, 4,7,11,15]
# [14,13,11,8, 4, 0]

# def twoSum(nums, target):
#     nums_dict = {}    # 字典存放(数值:下标)
#     for i in range(len(nums)):
#         temp = target - nums[i]  # temp存放差值
#         if temp in nums_dict:
#             return [i, nums_dict[temp]]
#         else:
#             nums_dict[nums[i]] = i
#
# l = [1,2,4,7,11,15]
# print(twoSum(l,15))

# def twosum(nums,target):
#     nums.sort()
#
#     begin = 0
#     end = len(nums)-1
#     while begin < end:
#         curr = nums[begin] + nums[end]
#         if curr == target:
#             print(nums[begin],nums[end])
#             begin += 1
#             end -= 1
#             # break
#         else:
#             if curr < target:
#                 begin += 1
#             else:
#                 end -= 1
#
#
# l = [1,2,4,7,11,13,15]
# twosum(l,15)