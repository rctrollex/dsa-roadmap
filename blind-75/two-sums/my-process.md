# 1. Two Sum

**Goal:** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

## The Thought Process

### Human Intuition
1. Look for numbers less than the target.
2. Loop through the remaining numbers by picking 1 and adding the next elements until we reach the target.
3. Keep track of their positions (indices) so they can be outputted.

### Algorithm Draft
1. Initialize the output list and find the length of the list.
2. Iterate through the length of the list to pick the first number.
3. Iterate a nested loop of `nums` and check if adding the two elements reaches the target.
4. Append those indices to the list.
5. Return the list.

## Attempt 1: The Working Brute-Force Solution

**Result:** Accepted on LeetCode! 

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output =[]
        length = len(nums)

        for i in range(length):
            # Enumerate helps track the index of the sliced list
            for index, num in enumerate(nums[i+1:]):
                if nums[i] + num == target:
                    output.append(i)
                    output.append(index + i + 1) # Math to find the original index
        return output
```

### Limitations & Code Analysis

While this solution works and was accepted, it is not optimized:

1. **Time Complexity is $O(n^2)$:** Because there is a `for` loop inside another `for` loop, the computer is doing a massive amount of repetitive checking. If the array is very large, this becomes incredibly slow.
2. **The List Slicing Trap:** `nums[i+1:]` forces Python to create a brand new copy of the list in memory on every single iteration of the outer loop. This hurts both Time Complexity and Space Complexity.

**Next Steps for Optimization:**
Goal is to drop the nested loop and achieve $O(n)$ time complexity using a Hash Map (Dictionary) to remember numbers and their indices in a single pass.