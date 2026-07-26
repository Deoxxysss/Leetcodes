class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)

        nums = [x for x in nums if count[x] == 1]

        return nums[0]