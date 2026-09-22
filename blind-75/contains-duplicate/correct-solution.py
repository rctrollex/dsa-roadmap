## What I learned is that you can buy speed by spendng memory.
## This is called Time-Space Trade Off
## Instead of using nested loop we can use a set to store the numbers we have seen so far.
## A list checks for items by looking at every single element one by one
## A set uses math(hashing) to place an item in a specific memory slot, it takes O(1) even the list has 5 items or 5 millions.

def containsDuplicates(nums):
    if len(nums) == 0:
        return False

    numbers = set()

    for num in nums:
        if num in numbers:
            return True

        numbers.add(num)
    return False
