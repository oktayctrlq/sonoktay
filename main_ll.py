#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 00:51:48 2025

@author: ctrlq
"""

# main_LL.py

from ds import LinkedListNode, Stack

# Stack oluştur
s = Stack()

# Push işlemleri
s.push(LinkedListNode("first"))
s.push(LinkedListNode("second"))
s.push(LinkedListNode("third"))

# Peek işlemi
print("Top of stack:", s.peek().data)  # third

# Pop işlemi
print("Popped:", s.pop().data)         # third

# Yeni top
print("New top:", s.peek().data)       # second
