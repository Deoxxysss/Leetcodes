class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        lst = []
        for i in range(nums[0], nums[len(nums)-1]+1):
            if i not in nums:
                lst.append(i)
        return lst
