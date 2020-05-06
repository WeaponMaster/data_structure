""" A Stack using a Linked List like structure """
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None):
        self.data: Any = data
        self.next: Optional["Node"] = next

    def __repr__(self):  # string representation of a Node
        return f"Node({self.data})"  # 字符串格式化输出


class LinkedStack:

    def __init__(self) -> None:
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item: Any) -> None:
        node: Node = Node(item)
        if self.is_empty():
            self.top = node
        else:
            # each node points to the item "lower" in the stack
            node.next = self.top
            self.top = node

    def pop(self) -> Any:
        """ returns and removes item at top of stack """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            # "remove" element by having top point to the next one
            assert isinstance(self.top, Node)
            node: Node = self.top
            self.top = node.next
            return node.data

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
