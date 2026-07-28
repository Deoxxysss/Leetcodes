class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        return (nums[i]-1)*(nums[i-1]-1)
