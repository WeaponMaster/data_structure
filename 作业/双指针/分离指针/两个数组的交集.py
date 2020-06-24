"""
349 - 两个数组的交集
题目描述
给定两个数组，编写一个函数来计算它们的交集。

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

说明:
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。


"""
from typing import List


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 排序
    nums1.sort()
    nums2.sort()

    i, j = 0, 0
    nums_set = set()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] == nums2[j]:
            nums_set.add(nums1[i])
            i += 1
            j += 1

    return list(nums_set)