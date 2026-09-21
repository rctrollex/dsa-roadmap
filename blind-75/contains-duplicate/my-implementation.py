
# def containsDuplicate(nums):
#     length = len(nums)
#
#     if length = =0:
#         return False
#
#     for i in range (length):
#         item = nums[i]
#         for num in nums[i:]:
#             if item == num:
#                 return True
#                 break
#             else:
#                 return False
#
#
# nums =[1 ,1 ,1 ,3 ,3 ,4 ,3 ,2 ,4 ,2]
# print(containsDuplicate(nums))

# This was my first implementation and this one had two Problems
    # 1. It was comparing the element with itself instead of going to the next element
    # 2. It was having a premature exit of the loop like when encounter the else it returns false

# Below code fixes this the solution is not efficient because it has a time complexity of O(n^2) by using two nested loops


def containsDuplicate(nums):
    length = len(nums)

    if length == 0:
        return False

    for i in range(length - 1):
        item = nums[i]
        for num in nums[i + 1:]:
            if item == num:
                return True
                break

    return False