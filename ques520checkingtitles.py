class Solution(object):
    def detectCapitalUse(self, word):
        r = len(word)
        if word[0].isupper():
            if all(word[i].isupper() for i in range(1, r)):
                return True
            elif all(word[i].islower()for i in range(1, r)):
                return True
            else:
                return False
        else:
            if all(word[i].islower() for i in range(0, r)):
                return True
            else:
                return False