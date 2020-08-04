class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s=list(bin(num).replace("0b", ""))
        if(s[0]=='-'):
            return False
        s.reverse()
        
        c=x=0
        n=len(s)
        if(num==1):
            return True
        for i in range(0,n):
            if(s[i]=='1'):
                if(i%2==0):
                    c+=1
                else:
                    x+=1
        if(c==1 and x==0):
            return True
        else:
            return False
                        
        