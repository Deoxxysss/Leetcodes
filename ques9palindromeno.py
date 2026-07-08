class Solution:
    def isPalindrome(self, x: int) -> bool:
        if int(str(abs(x))[::-1]) == x:
            return True
        else:
            return False