class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        olas = 0
        while target != 1:
            if target%2 == 0 and maxDoubles != 0:
                olas += 1
                target = target//2
                maxDoubles -= 1
            elif maxDoubles == 0:
                n = target//1
                target -= (n-1)
                olas += n-1
            else:
                olas += 1
                target -= 1
        return olas