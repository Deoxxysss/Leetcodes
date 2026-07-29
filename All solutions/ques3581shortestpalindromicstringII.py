import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1  # k max is 10^6, cap here to avoid big ints

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        # Step 1: Build half counts and find middle character
        halfCount = [0] * 26
        mid = ''
        for c, freq in count.items():
            halfCount[ord(c) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid = c
        
        # Step 2: Check if k is valid
        total = self._countArrangements(halfCount)
        if k > total:
            return ''
        
        # Step 3: Greedily build the left half
        halfLen = sum(halfCount)
        left = []
        for _ in range(halfLen):
            for i in range(26):
                if halfCount[i] == 0:
                    continue
                # Try placing char i at this position
                halfCount[i] -= 1
                arrangements = self._countArrangements(halfCount)
                if arrangements >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    halfCount[i] += 1  # undo, try next char
        
        # Step 4: Mirror to get full palindrome
        return ''.join(left) + mid + ''.join(reversed(left))
    
    def _countArrangements(self, count: list[int]) -> int:
        """Count distinct permutations of a multiset, capped at MAX."""
        total = sum(count)
        res = 1
        for freq in count:
            if freq == 0:
                continue
            res *= self._nCk(total, freq)
            if res >= self.MAX:
                return self.MAX
            total -= freq
        return res
    
    def _nCk(self, n: int, k: int) -> int:
        """Compute n choose k, capped at MAX."""
        if k < 0 or k > n:
            return 0
        k = min(k, n - k)
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX
        return res
