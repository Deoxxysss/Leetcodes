class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        x = 1
        while (x*x - x) // 2 < n:
            if (n/x + 0.5 - x/2) % 1 == 0:
                count += 1
            x += 1

        return count