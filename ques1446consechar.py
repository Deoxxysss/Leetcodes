class Solution:
    def maxPower(self, s: str) -> int:
        maximum = 1
        current = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                current = 1

            maximum = max(maximum, current)

        return maximum