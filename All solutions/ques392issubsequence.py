class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return  False
            p = t.find(i)
            t = t[p + 1:]
        return True
