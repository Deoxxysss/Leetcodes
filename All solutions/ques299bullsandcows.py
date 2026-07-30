from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        s = []
        g = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s.append(secret[i])
                g.append(guess[i])

        cs = Counter(s)
        cg = Counter(g)

        cows = 0
        for d in cs:
            cows += min(cs[d], cg[d])

        return f"{bulls}A{cows}B"
