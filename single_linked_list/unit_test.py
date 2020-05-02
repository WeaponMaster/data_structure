class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None
# 单个元素创建链表
    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        if self.head is None:
            insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    def insert(self,i,data):
        if self.head is None or i == 1:
            self.head = insert_head(data)

        else:
            new_node = Node(data)
            temp = self.head
            pre = temp
            j = 1
            while j < i:
                pre = temp
                temp = temp.next
            pre.next = new_node
            new_node.next = temp
# 直接构建多元素列表
    def linklist(self,object):
        new_node = Node(object[0])
        self.head = new_node
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next

    def delete_head(self):
        temp = self.head
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    # 辅助函数
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def __repr__(self):
        current = self.head
        string_repr = ""
        while  current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"

a = LinkList()
a.linklist([1,2,3])
a.print_list()
print(a)
a.delete_head()
print(a)