"""
Author:  Mr.Zhang
Create:  2020/6/14 0:01
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""


class Array():
    def __init__(self, capacity):
        self.array = [None] * capacity  # 数组的长度
        self.size = 0  # 数组有效元素的多少

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("数组越界")
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size-1, index, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1
        # 数组长度扩增

    def remove(self,index):
        if index<0 or index>self.size:
            raise Exception('数组越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2  # 为什么不使用capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='->')


array = Array(4)
array.insert(0, 0)
print(array.size)
array.insert(1, 1)
print(array.size)
array.insert(2, 2)
print(array.size)
array.insert(3, 3)
array.insert(4, 4)
print(array.size)
print('----')
array.output()
array.remove(1)
