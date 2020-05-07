# 导入typing包,用作类型注解
from typing import Any, Optional, NoReturn


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None): # next为可选类型,可为Node可为None
        self.data: Any = data
        self.next: Optional["Node"] = next

    def __repr__(self):  # string representation of a Node
        return f"Node({self.data})"  # 字符串格式化输出


class LinkedStack:
    def __init__(self) -> NoReturn:
        self.top: Optional[Node] = None

    def push(self, item: Any) -> None:
        node: Node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self) -> Any:
        if self.top is None:
            raise IndexError("pop from empty stack")
        else:
            assert isinstance(self.top, Node)
            node: Node = self.top
            self.top = node.next
            return node.data

    def is_empty(self) -> bool:
        return self.top is None

    def __repr__(self):  # String representation/visualization of a Linked Lists
        current = self.top
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        # END represents end of the LinkedList
        return string_repr + "END"


stack = LinkedStack()
stack.is_empty()
stack.push(5)
stack.push(9)
stack.push('python')
print(stack)
stack.pop()
print(stack)
