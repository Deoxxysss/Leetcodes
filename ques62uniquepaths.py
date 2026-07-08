class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = m + n - 2
        c = n - 1
        o = m - 1
        r = 1
        z = 1
        h = 1
        if t > 0 and c > 0 and o > 0:
            for _ in range(1, t+1):
                r = r*_
            for a in range(1, c+1):
                z = z*a
            for i in range(1, o+1):
                h = h*i
            return r//(z*h)
        else:
            return 1