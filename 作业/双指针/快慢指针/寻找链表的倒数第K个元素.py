"""
让快指针先走 k 步，然后快慢指针开始同速前进。这样当快指针走到链表末尾 null 时，
慢指针所在的位置就是倒数第 k 个链表节点
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def lastK(head, k):
    slow = head
    fast = head
    while k > 0:
        fast = fast.next
        k -= 1
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = None
    print('倒数第3个元素是:%s'%lastK(node1,3))