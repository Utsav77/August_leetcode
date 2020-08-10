class Solution:
    def titleToNumber(self, s: str) -> int:
        n=len(s)-1
        res=0
        for i in s:
            res+=(ord(i)-64)*(26**(n))
            n-=1
        return res
            