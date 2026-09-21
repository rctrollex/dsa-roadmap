# 217. Contains Duplicate

**Goal:** Given an integer array `nums`, return `True` if any value appears at least twice, and return `False` if every element is distinct.

## The Thought Process

### Human Intuition
1. Select the first element.
2. Check the remaining elements to see if they match.
    * If a match is found $\rightarrow$ return `True` and stop.
    * Else, continue checking until the list is finished and return `False`.

### Algorithm Draft
1. Find the length of the array.
2. If the array is empty, return `False`.
3. Iterate a loop to select the item we will check.
4. Iterate a second nested loop for the items we will check against.
    * If the value is the same, return `True`.
    * If the entire process finishes without a match, return `False` at the very end.

---

## Attempt 1: The Buggy Draft

```python
def containsDuplicate(nums):
    length = len(nums)

    if length == 0:
        return False

    for i in range(length):
        item = nums[i]
        for num in nums[i:]:
            if item == num:
                return True
                break
            else:
                return False
```

### What Went Wrong Here?
This initial implementation had two critical bugs:
1. **Self-Comparison:** By looping through `nums[i:]`, the inner loop included the current element. It immediately compared the item against itself, resulting in a false positive on the very first check.
2. **Premature Exit:** The `else: return False` block forced the function to exit immediately after checking just one single pair of numbers, rather than waiting until all checks were complete.

---

## Attempt 2: The Working Brute-Force Solution

This updated implementation fixes the self-comparison by slicing the array from the *next* element `nums[i + 1:]`, and fixes the premature exit by moving `return False` to the very end of the function.

```python
def containsDuplicate(nums):
    length = len(nums)

    if length == 0:
        return False

    # length - 1 because the last element has nothing after it to compare against
    for i in range(length - 1):
        item = nums[i]
        
        # Check only the elements that come AFTER the current item
        for num in nums[i + 1:]:
            if item == num:
                return True
                # break  <-- Removed: Unreachable code since `return` instantly exits the function

    # If all loops finish without triggering True, there are no duplicates
    return False
```

### Current Status
**Result:** Logically correct, but inefficient. 
**Time Complexity:** $O(n^2)$ because of the two nested loops. For very large arrays, this will result in a "Time Limit Exceeded" error.
It reached time complexity after 65 tries on leetcode