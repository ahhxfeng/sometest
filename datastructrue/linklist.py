#! /bin/env/ python
# 链表的实现
#coding=utf-8
#author="ahhxfeng"
#version=1.0

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkList():
    """
    init linklist
    """
    def __init__(self):
        self.head = Node(None)

    def init_list(self, list_):
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next

    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
    
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    def delete(self, x):
        p = self.head
           # 　结束循环必然两个条件其一为假
        while p.next and p.next.val != x:
           p = p.next
        if p.next is None:
           raise ValueError("x not in linklist")
        else:
           p.next = p.next.next

    #　获取某个节点值,传入节点位置获取节点值
    def get_index(self,index):
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val

if __name__ == "__main__":
    list1 = LinkList()
    a = [0, 5, 2, 6, 9]
    list1.init_list(a)
    list1.show()