"""
15 - 三数之和
题目描述
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如，给定数组 nums = [-1, 0, 1, 2, -1, -4]，满足要求的三元组集合为：

[
  [-1, 0, 1],
  [-1, -1, 2]
]

思路
我们可以先对数组进行排序，然后我们选择一个数字做 C 位，然后我们在这个 C 位数字的右边进行双指针搜索：

从最左边 i+1（最小值）和最右边 len(nums)-1（最大值）两个数字开始，加上 C 位，计算总和是否等于 0。
如果大于 0，说明实力太强了，就把右侧的数字左移一位。
如果小于 0，说明实力太弱了，就把左边的数字右移一位。
当双指针碰到的时候，这轮循环结束，以该数字为 C 位的所有可能都已经尝试完毕了。
这里要注意数组的去重，去重过程包含了遍历，也会增加时间复杂度，所以我进行了优化，
对于排序完成的数组来说，只要判断下相邻的数是否相等，如果相等就直接移动指针即可，这就完成了去重。
"""


def threeSum(nums):
    # 排序
    nums.sort()

    # 单循环+双指针
    res = []

    for i in range(len(nums)-2):
        # 去重（如果当前C位数和相邻的数相等，直接移动指针）
        # [-1, -1, 1, 2, -1, -4]
        if i > 0 and nums[i] == nums[i - 1]:
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
                # 去重（如果当前数和相邻的数相等，直接移动指针）
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))










