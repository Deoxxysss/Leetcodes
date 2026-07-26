class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = []

        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)

        ans = []

        for i in range(len(s)):
            mini = float('inf')
            for p in positions:
                mini = min(mini, abs(i - p))
            ans.append(mini)

        return ans