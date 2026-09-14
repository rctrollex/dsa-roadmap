# Linked Lists Overview

Welcome to the main linked list directory. 

A linked list is a linear data structure where elements (nodes) are not stored at contiguous memory locations. Instead, each node points to the next, forming a chain. This structure allows for efficient insertions and deletions compared to standard arrays.

This document serves as a high-level overview of the three primary types of linked lists: **Singly**, **Doubly**, and **Circular**. You will find deeper, code-heavy implementations and specific operations in their respective subdirectories (`/singly`, `/doubly`, etc.).

---

## 1. Singly Linked List

A singly linked list is the simplest type of linked list. Each node contains two parts:
1. **Data:** The actual value or information stored.
2. **Next Pointer:** A reference to the next node in the sequence.

Traversal in a singly linked list is strictly unidirectional (forward only). The last node's `next` pointer points to `None` (or `null`), indicating the end of the list.

### Node Structure Definition
```python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
```

---

## 2. Doubly Linked List

A doubly linked list extends the singly linked list by adding an extra pointer. Each node contains three parts:
1. **Data:** The stored value.
2. **Next Pointer:** A reference to the next node.
3. **Prev Pointer:** A reference to the previous node.

This bidirectional structure allows for traversal in both forward and backward directions, making certain operations (like deleting a given node or traversing backwards) much more efficient, though it requires extra memory for the `prev` pointer.

### Node Structure Definition
```python
class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
```

---

## 3. Circular Linked List

A circular linked list is a variation where the last node does not point to `None`. Instead, the `next` pointer of the last node loops back and points to the `head` (the first node), forming a continuous circle. 

Circular linked lists can be either singly circular or doubly circular. They are particularly useful for applications that require continuous looping, such as round-robin scheduling algorithms or multiplayer board game turns.

### Node Structure Definition (Singly Circular)
The node structure is identical to a singly linked list, but the list logic ensures the tail connects to the head.
```python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node # In a circular list, the tail's next is set to head
```

---

## Comparison Table

| Feature | Singly Linked List | Doubly Linked List | Circular Linked List |
| :--- | :--- | :--- | :--- |
| **Traversal Direction** | Unidirectional (Forward only) | Bidirectional (Forward & Backward) | Continuous/Looping (Forward, or both if doubly circular) |
| **Pointers per Node** | 1 (`next`) | 2 (`next`, `prev`) | 1 or 2 (Depends on singly or doubly circular) |
| **Memory Overhead** | Low (Only one pointer) | High (Requires extra pointer per node) | Low to High |
| **End Node Pointer** | Points to `None` | Points to `None` | Points back to the `head` node |
| **Complexity of Deletion**| $O(n)$ to find the previous node | $O(1)$ if the node to delete is known | $O(n)$ generally, requires maintaining the circle |
| **Best Use Case** | Basic sequential data, implementing stacks/queues | Complex navigation, browser history, music playlists | CPU scheduling, continuous looping structures |

---

## Next Steps

To dive deeper into the specific mechanics, edge cases, and full class implementations (including methods like `insert_at_head`, `delete_node`, and `traverse`), please explore the subfolders:
* `/singly`
* `/doubly`
* `/circular`