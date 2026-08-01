from functools import cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        ...

        @cache
        def dp(i, j):
            if i == j:
                return nums[i]

            left = nums[i] - dp(i + 1, j)
            right = nums[j] - dp(i, j - 1)

            return max(left, right)

        return dp(0, len(nums) - 1) >= 0
