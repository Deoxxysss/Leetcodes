class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-' and int(str(abs(x))[::-1]) <= 2**31:
            return -(int(str(-x)[::-1]))
        elif str(x)[0] != '-' and int(str(x)[::-1]) <= 2**31 - 1:
            return (int(str(x)[::-1]))
        else:
            return 0