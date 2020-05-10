"""
Author:  Mr.Zhang
Create:  2020/5/9 9:18
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""
from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent  # Added in order to delete a node easier
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None: # self.node is None
            return True
        else:
            return False

    def __insert(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:  #
                if value < parent_node.value:  # 如果插入值小于父结点的值
                    if parent_node.left is None:  # 如果父节点的左结点是空
                        parent_node.left = new_node  # 把插入值设为左节点
                        break
                    else:
                        parent_node = parent_node.left  # 如果父节点左侧不空,那么判断结点下移
                else:  # 如果插入值大于父结点的值
                    if parent_node.right is None:  # 如果父结点是空
                        parent_node.right = new_node # 把插入值设为右节点
                        break
                    else:
                        parent_node = parent_node.right # 如果父节点右侧不空,那么判断结点下移
            new_node.parent = parent_node  # 指定一下新结点的父结点

    def insert(self, *values):
        for value in values:
            self.__insert(value)
        return self

    def search(self, value):
        if self.is_empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            print(node)
            return node

    def is_right(self, node):
        return node == node.parent.right

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:  # 先把当前节点的孩子父结点设为当前节点的父结点->节点上移
            new_children.parent = node.parent
        if node.parent is not None:  # reset its parent
            if self.is_right(node):  # If it is the right children
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self, value):
        node = self.search(value)  # Look for the node with that label
        if node is not None:
            if node.left is None and node.right is None:  # 没有孩子节点的情况
                self.__reassign_nodes(node, None)  # 交换当前节点和None->当前节点变成空
            elif node.left is None:  # 只有右侧孩子节点
                self.__reassign_nodes(node, node.right)  #
            elif node.right is None:  # 只有左侧孩子节点
                self.__reassign_nodes(node, node.left)
            else:
                tmp_node = self.get_max(node.left)  # Gets the max value of the left branch
                self.remove(tmp_node.value)
                node.value = tmp_node.value  # Assigns the value to the node to delete and keep tree structure

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node

    def preorder(self, node):
        """self, left, right"""
        if node is not None:
            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def inorder(self, node):
        """left,self,right"""
        if node is not None:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)

    def postorder(self, curr_node):
        """left, right, self"""
        node_list = list()
        if curr_node is not None:
            node_list = self.postorder(curr_node.left) + self.postorder(curr_node.right) + [curr_node]
        return node_list

    def traversal(self, method=None):
        """遍历方法,需要指定遍历策略"""
        if method == 'pre':
            return self.preorder(self.root)
        elif method == 'post':
            return self.postorder(self.root)
        else:
            return self.inorder(self.root)


t = BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
print(" ".join(repr(i.value) for i in t.traversal(method='pre')))
print(" ".join(repr(i.value) for i in t.traversal(method='post')))
print(" ".join(repr(i.value) for i in t.traversal(method='in')))
t.search(6)
# t.remove(13)
# print(" ".join(repr(i.value) for i in t.traversal()))

"""
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13

"""
# testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
# t = BinarySearchTree()
# for i in testlist:
#     t.insert(i)
# print(t)
"""


if t.search(6) is not None:
    print("The value 6 exists")
else:
    print("The value 6 doesn't exist")

if t.search(-1) is not None:
    print("The value -1 exists")
else:
    print("The value -1 doesn't exist")

if not t.is_empty():
    print("Max Value: ", t.get_max().value)
    print("Min Value: ", t.get_min().value)

for i in testlist:
    t.remove(i)
    print(t)
"""
