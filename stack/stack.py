"""
:Author:  Mr.Zhang
:Create:  2020/5/4 10:25
:Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""


class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        """ Peek at the top-most element of the stack."""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def size(self):
        """ Return the size of the stack."""
        return len(self.stack)


class StackOverflowError(BaseException):
    print("StackOverFlow栈溢出")


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print("stack demonstration:\n")
    print("Initial stack: " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.size()))
    stack.push(100)
