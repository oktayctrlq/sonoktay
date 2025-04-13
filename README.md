# OKTAY DUMAN - 2200674014


# 🧱 Custom Stack Implementation Using Linked List in Python

Hello! 👋  
This repository contains a custom implementation of a **Stack** data structure using a manually created **Singly Linked List** in Python. I built this from scratch to reinforce my understanding of core data structures and object-oriented programming concepts without relying on Python’s built-in list or `deque` types.

I aimed to deeply explore how nodes interact within a linked list and how I can implement `push`, `pop`, and `peek` functionalities just like a real stack (LIFO: Last In First Out).

---

## 📁 Project Structure

| File Name     | Description |
|---------------|-------------|
| `ds.py`       | Contains class definitions for `Node`, `LinkedListNode`, `LinkedList`, and `Stack` |
| `main_LL.py`  | A sample script that tests the stack operations using the classes from `ds.py` |

---

## 📌 Purpose of the Project

The main goal of this project was to **manually build** a stack using basic class definitions, constructor chaining, and linked node operations. While Python provides abstract data types like `list` and `deque`, I deliberately avoided using them to strengthen my understanding of:

- Object-oriented design
- Node and pointer logic (through `next`)
- Custom class design patterns
- Data manipulation using user-defined structures

---

## 🧱 Core Classes Explained

| Class Name       | Responsibility |
|------------------|----------------|
| `Node`           | A base class to hold generic data |
| `LinkedListNode` | Extends `Node`, adding a `next` pointer to link to the next node |
| `LinkedList`     | Handles inserting and removing nodes by index, used internally by `Stack` |
| `Stack`          | Implements `push`, `pop`, and `peek` operations using the `LinkedList` |

---

## 🧪 Sample Usage

Here’s a simple demonstration of how I used the `Stack` and `LinkedListNode` classes to add and remove elements from a stack:

```python
from ds import LinkedListNode, Stack

# Creating a new stack instance
s = Stack()

# Pushing elements
s.push(LinkedListNode("first"))
s.push(LinkedListNode("second"))
s.push(LinkedListNode("third"))

# Peeking the top element
print("Top of stack:", s.peek().data)  # Output: third

# Popping the top element
print("Popped:", s.pop().data)         # Output: third

# New top after popping
print("New top:", s.peek().data)       # Output: second
