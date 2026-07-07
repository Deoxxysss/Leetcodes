class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        digits = []

        while n > 0:
            digits.append(n % 10)  
            n //= 10 
        gola = 0
        mola = 1 
        for i in digits:
            gola +=i
            mola = mola*i
        return mola - gola