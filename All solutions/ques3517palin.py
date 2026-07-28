class Solution(object):
    def smallestPalindrome(self, s):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        left = []
        mid = ""

        for i in range(26):
            left.append(chr(ord('a') + i) * (cnt[i] // 2))
            if cnt[i] % 2:
                mid = chr(ord('a') + i)

        left = "".join(left)
        return left + mid + left[::-1]
        
