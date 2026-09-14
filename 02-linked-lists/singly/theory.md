# Singly Linked List Implementation Guide

## Structure of a Singly Linked List

A singly linked list is a linear data structure built from independent objects called **Nodes**. Unlike an array, these nodes do not sit next to each other in memory. Instead, they rely on pointers to maintain their sequence.

Each node contains exactly two components:
1. **Data:** The actual value being stored (e.g., an integer, a string, or an object).
2. **Next Pointer:** A reference that points to the memory location of the next node in the sequence. 

The entire list is controlled by a single pointer called the **Head**, which points to the very first node. The final node in the list points to `None`, indicating the end of the chain. Because the pointers only go in one direction, you can only traverse a singly linked list strictly forward.

---

## Time Complexity

Because nodes are scattered in memory, accessing elements requires starting at the head and walking through the chain one by one. Here is the time complexity for standard operations based on your specific implementation (which only tracks the `head` pointer):

| Operation | Time Complexity | Explanation |
| :--- | :--- | :--- |
| **Find/Access at Start (Index 0)** | $O(1)$ | Directly accessible via the `head` pointer. |
| **Find/Access at Index $k$** | $O(n)$ | Requires traversing $k$ nodes from the head to reach the target. |
| **Find/Access at End** | $O(n)$ | Requires traversing the entire list until `next` is `None`. |
| **Insert/Delete at Start** | $O(1)$ | Simply reassigning the `head` pointer to a new node or the next node. |
| **Insert/Delete at Index $k$ or End** | $O(n)$ | Must traverse the list to find the element just before the target location. |

---

## Method Breakdown & Algorithms

Here is an explanation of every method in your Python code, detailing what it does, how it works, and the underlying algorithm.

### 1. `__init__` (Node and LinkedList)
* **What it does:** Initializes the foundational building blocks.
* **How it works:** The `Node` class sets up the `data` and `next` attributes. The `LinkedList` class sets up the `head` pointer and initializes it to `None` (representing an empty list).

### 2. `insert_at_begining(self, data)`
* **What it does:** Adds a new node to the very front of the linked list.
* **How it works:** It creates a new node, points this new node's `next` to the current `head`, and then updates the `head` pointer to be this new node.
* **Algorithm:**
  1. Create a new Node with `data`.
  2. Set the new Node's `next` pointer to the current `head`.
  3. Reassign `head` to the new Node.

### 3. `print(self)`
* **What it does:** Traverses the list and prints the elements sequentially as a string chain.
* **How it works:** It uses a temporary pointer (`itr`) starting at the `head` and loops until `itr` becomes `None`.
* **Algorithm:**
  1. Check if `head` is `None`. If yes, print "Linked list is empty" and return.
  2. Set `itr` to `head`.
  3. Initialize an empty string `llstr`.
  4. While `itr` is not `None`:
     * Append `itr.data` and `'-->'` to `llstr`.
     * Move `itr` to the next node (`itr = itr.next`).
     * Print `llstr`.

### 4. `insert_at_end(self, data)`
* **What it does:** Appends a new node to the very end of the list.
* **How it works:** If the list is empty, it assigns the new node directly to the head. Otherwise, it traverses the entire list until it finds the last node (where `next` is `None`) and links the new node there.
* **Algorithm:**
  1. If `head` is `None`, set `head` to the new Node and return.
  2. Set `itr` to `head`.
  3. While `itr.next` is not `None`, move `itr` forward (`itr = itr.next`).
  4. Set `itr.next` to the new Node.

### 5. `insert_values(self, data_list)`
* **What it does:** Replaces the current linked list with a fresh list built from a Python array/list.
* **How it works:** It clears the current list by setting `head` to `None`, then iterates through the provided array, calling `insert_at_end` for each item.
* **Algorithm:**
  1. Set `head` to `None`.
  2. For each element in `data_list`:
     * Call `insert_at_end(element)`.

### 6. `get_length(self)`
* **What it does:** Calculates the total number of nodes in the list.
* **How it works:** It traverses the list from the head to the end, incrementing a counter variable at each node.
* **Algorithm:**
  1. Initialize `count = 0`.
  2. Set `itr` to `head`.
  3. While `itr` is not `None`:
     * Increment `count` by 1.
     * Move `itr` to the next node.
  4. Return `count`.

### 7. `remove_at(self, index)`
* **What it does:** Deletes a node at a specific index.
* **How it works:** It first checks if the index is valid. If removing index 0, it simply moves the `head` pointer forward. For any other index, it stops exactly one node *before* the target index and routes its `next` pointer around the target node to skip it.
* **Algorithm:**
  1. If `index < 0` or `index >= list_length`, throw an Exception.
  2. If `index == 0`, set `head` to `head.next` and return.
  3. Set `itr` to `head` and `count` to 0.
  4. While `itr` is not `None`:
     * If `count == index - 1`:
       * Set `itr.next = itr.next.next` (bypassing the target node).
       * Break the loop.
     * Move `itr` to the next node and increment `count`.

### 8. `insert_at(self, index, data)`
* **What it does:** Inserts a new node at a specific index position.
* **How it works:** Similar to `remove_at`, it validates the index and handles head insertion explicitly. For middle insertions, it traverses to the node exactly one step before the target index, creates the new node pointing to the current node's `next`, and updates the current node to point to the new node.
* **Algorithm:**
  1. If `index < 0` or `index > list_length`, throw an Exception.
  2. If `index == 0`, call `insert_at_begining(data)` and return.
  3. Set `itr` to `head` and `count` to 0.
  4. While `itr` is not `None`:
     * If `count == index - 1`:
       * Create a new Node with `data` and its `next` pointing to `itr.next`.
       * Set `itr.next` to point to the new Node.
       * Break the loop.
     * Move `itr` to the next node and increment `count`.