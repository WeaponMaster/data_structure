"""
0 & 0 = 0
1 & 1 = 1
1 & 0 = 0

0 | 0 = 0
1 | 0 = 1
1 | 1 = 1

1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 0 = 0

n & (n-1) 能够消灭 n 中最右侧的一个 1。
右移：除以 2；左移：乘以 2。
异或性质：交换律，0^a=a, a^a=0。
将常用字符、数字等均转为按位运算，可以节约空间

191 - 位 1 的个数
问题描述
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

"""
class Solution:
    def hammingWeight(self,n):
        count = 0
        while n!=0:
            n = n&(n-1)
            count+=1
        return count