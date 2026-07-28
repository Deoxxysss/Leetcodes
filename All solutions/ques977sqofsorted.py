class Solution(object):
    def sortedSquares(self, nums):
        bala = [i**2 for i in nums]
        return sorted(bala)
        
