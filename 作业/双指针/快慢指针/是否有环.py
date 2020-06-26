class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def is_circle(head):
    curr = head
    prev = head
    while curr and curr.next:
        curr = curr.next.next
        prev = prev.next
        if prev == curr:
            return True
    return False


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node1
    print(is_circle(node1))