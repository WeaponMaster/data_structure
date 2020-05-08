"""
:Author:  Mr.Zhang
:Create:  2020/5/8 11:15
:Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(root, data):
    new_node = Node(data)
    new_node.left = None
    new_node.right = None
    if root is None:
        root = new_node
        return root
    else:
        current = root
        while current is not None:
            backup = current
            if current.data > data:
                current = current.left
            else:
                current = current.right
        if backup.data > data:
            backup.left = new_node
        else:
            backup.right = new_node
    return root


def display(tree):  # In Order traversal of the tree

    if tree is None:
        return

    if tree.left is not None:
        display(tree.left)

    print(tree.data)

    if tree.right is not None:
        display(tree.right)

    return


# This is the recursive function to find the depth of binary tree.
def depth_of_tree(tree,):
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(tree):
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return is_full_binary_tree(
            tree.left) and is_full_binary_tree(
            tree.right)
    else:
        return False


data = [5, 6, 24, 8, 12, 3, 17, 1, 9]
ptr = None
root = None
for i in range(9):
    ptr = create_tree(ptr, data[i])
display(ptr)
