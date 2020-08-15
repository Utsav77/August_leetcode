class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        c=0
        for i in d:
            if(d[i]%2==0):
                c+=d[i]
            else:
                c+=d[i]-1
        if(len(s)==c):
            return c
        else:
            return c+1
        