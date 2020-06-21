"""
LeetCode 80 - 删除排序数组中的重复项
题目描述
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3], 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3], 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。

思路
遍历整个表：

把当前的元素与它前面的对比，如果二者元素相同（为重复元素）：
此时统计重复的计数器 count+=1。题目要求只保留 2 个重复的元素，这里需要加入重复元素个数的判断：

这个元素正好重复了 2 次 => 则进行保留。列表长度 i+=1，然后 nums[i]=nums[j]；
这个元素重复多于 2 次 => 不进行任何操作。体现在程序上不做处理
把当前的元素与它前面的对比，如果二者元素不同（为新元素）：此时把当前这个结点 (nums[j]) 添加到新表里面去，nums[i] = nums[j], 表长 i+1
"""
from typing import List

class Solution:
    def removeDuplicated(self,nums: List[int])->int:
        count = 1
        slow = 0
        fast = 1
        # [1,1,1,2,2,3,4]
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                count = 1
                fast += 1
        return slow + 1