class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        elif n < 0:
            return False
        else:
            for i in range(31):
                if 2**i == n:
                    return True
            return False
