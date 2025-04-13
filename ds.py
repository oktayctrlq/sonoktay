#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 00:51:15 2025

@author: ctrlq
"""

# ds.py

class Node:
    def __init__(self, data):
        self.data = data

class LinkedListNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node, index):
        if index == 0:
            node.next = self.head
            self.head = node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        node.next = current.next
        current.next = node

    def remove_node(self, index):
        if self.head is None:
            raise IndexError("Empty list")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        current.next = current.next.next

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, node):
        self.ll.add_node(node, 0)

    def pop(self):
        if self.ll.head is None:
            return None
        top = self.ll.head
        self.ll.remove_node(0)
        return top

    def peek(self):
        return self.ll.head
