class Solution(object):
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    lst.extend([i, j])
                    return lst
            else:
                continue