"""


Parameters
----------

Returns
-------

:Author:  Mr.Zhang
:Create:  2020/5/2 10:38
:Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""

class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None

    def __repr__(self):  # string representation of a Node
        return f"Node({self.data})"  # 字符串格式化输出


class LinkedList:
    def __init__(self):
        self.head = None  # initialize head to None

    def append(self, data) -> None:
        if self.head is None:
            self.insert_head(data)  # if this is first node, call insert_head
        else:
            temp = self.head
            while temp.next:  # traverse to last node
                temp = temp.next
            temp.next = Node(data)  # create node & link to tail

    def insert_head(self, data) -> None:
        """
        :param data:
        :type data:
        :return:
        :rtype:
        """
        new_node = Node(data)  # create a new node
        if self.head:  # 如果有头部结点
            new_node.next = self.head  # link new_node to head
        self.head = new_node  # make NewNode as head

    def insert(self, i, data):
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            pre = temp
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp

    def linklist(self, object)-> None:
        """
        :param object:
        :type object:
        :return:
        :rtype:
        """
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next

    def print_list(self) -> None:  # print every node data
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_head(self):  # delete from head
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        temp = self.head
        if self.head:
            if self.head.next is None:  # if head is the only Node in the Linked List
                self.head = None
            else:
                while temp.next.next:  # find the 2nd last element
                    temp = temp.next
                # (2nd last element).next = None and temp = last element
                temp.next, temp = None, temp.next
        return temp

    def is_empty(self) -> bool:
        return self.head is None  # return True if head is none

    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    def __repr__(self):  # String representation/visualization of a Linked Lists
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        # END represents end of the LinkedList
        return string_repr + "END"

    # Indexing Support. Used to get a node at particular position
    def __getitem__(self, index):
        current = self.head

        # If LinkedList is empty
        if current is None:
            raise IndexError("The Linked List is empty")

        # Move Forward 'index' times
        for _ in range(index):
            # If the LinkedList ends before reaching specified node
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        return current

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        current = self.head
        # If list is empty
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data


a = LinkedList()
a.linklist([1, 2, 3])
a.insert(1,0)
a.insert(5,4)
# a.append(2)
# a.append(3)
# a.append(5)
print(a)
# a.insert(4,4)
# print(a)