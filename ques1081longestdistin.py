class Solution:
    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter

        count = Counter(s)
        stack = []
        in_stack = set()

        for ch in s:
            count[ch] -= 1

            if ch in in_stack:
                continue

            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                in_stack.remove(stack.pop())

            stack.append(ch)
            in_stack.add(ch)

        return "".join(stack)
        