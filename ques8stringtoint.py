class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        if s[0] in "+-":
            if s[0] == "-":
                sign = -1
            s = s[1:]

        num = ""

        for ch in s:
            if ch.isdigit():
                num += ch
            else:
                break

        if not num:
            return 0

        ans = sign * int(num)

        return max(-2**31, min(ans, 2**31 - 1))
