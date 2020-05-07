"""
:Author:  Mr.Zhang
:Create:  2020/5/7 23:15
:Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""

from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None):
        self.data: Any = data
        self.next: Optional["Node"] = next

    def __repr__(self):  # string representation of a Node
        return f"Node({self.data})"  # 字符串格式化输出


class LinkedQueue:

    def __init__(self) -> None:
        self.front: Optional[Node] = None  # 头结点
        self.rear: Optional[Node] = None  # 尾结点

    def is_empty(self) -> bool:
        return self.front is None

    def put(self, item: Any) -> None:
        node: Node = Node(item)
        if self.is_empty():
            self.front = node  # 只包含一个结点的情况,前后都指向同一个结点
            self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node  # 尾结点后增加一个结点
            self.rear = node  # 尾结点后移

    def pop(self):
        if self.is_empty():
            raise IndexError("delete from empty queue")
        else:
            node: Node = self.front
            self.front = node.next

    def get(self) -> Any:
        if self.is_empty():
            raise IndexError("get from empty queue")
        else:
            # "remove" element by having front point to the next one
            assert isinstance(self.front, Node)
            node: Node = self.front
            self.front = node.next
            if self.front is None:
                self.rear = None

            return node.data

    def __repr__(self):
        current = self.front
        string_repr = ""
        while current:
            string_repr += f"{current} <-- "
            current = current.next
        # END represents end of the LinkedList
        return string_repr + "END"


queue = LinkedQueue()
queue.put(1)
queue.put(2)
queue.put("python")
queue.put("java")
print(queue)
queue.pop()
print(queue)