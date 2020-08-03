class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        if(s==''):
            return True
        for i in s:
            if(i.isalnum()):
                res+=i
        if(res.lower()==res[::-1].lower()):
            return True
        else:
            return False