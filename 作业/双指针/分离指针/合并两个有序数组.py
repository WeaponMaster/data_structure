"""
88 - 合并两个有序数组
https://leetcode-cn.com/problems/merge-sorted-array/
题目描述
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""
from typing import List


def mergeTwo(nums1: List[int], m: int, nums2: List[int], n: int):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:  # nums2遍历完之后
            nums1[k] = nums1[i]
            i -= 1
            # k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            # k -= 1
        k -= 1
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return
