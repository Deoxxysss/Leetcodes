class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums)-1
        if nums[0] * nums[1] * nums[right] > nums[right-2] * nums[right] * nums[right - 1]:
            return nums[0] * nums[1] * nums[right]
        return nums[right-1]*nums[right]*nums[right-2]
