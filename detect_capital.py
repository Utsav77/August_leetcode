class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.isupper()):
            return True
        elif(word.islower()):
            return True
        elif(word[:1].isupper()):
            if(word[1:].islower()):
                return True
        