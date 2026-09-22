class Solution:
    def twoSum(self, nums, target):
        output =[]
        length= len(nums)

        for i in range(length):
            for index, num in enumerate(nums[i+1:]):
                if nums[i]+num==target:
                    output.append(i)
                    output.append(index+i+1)
        return output