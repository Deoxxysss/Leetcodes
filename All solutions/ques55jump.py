class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        
        for i in range(len(nums)):
            if i <= farest:
                farest = max(farest, i + nums[i])
            
            if farest >= len(nums) - 1:
                return True
        
        return False