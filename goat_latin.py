class Solution:
    def toGoatLatin(self, S: str) -> str:
        a=list(S.split())
        res=''
        for i in range(0,len(a)):
            if(len(a[i])>1):
               j=a[i][:1].lower()
            else:
               j=a[i].lower()
            
            if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
                res+=a[i]+'ma'
            else:
                res+=a[i][1:]
                res+=a[i][:1]
                res+='ma'
            for k in range(i+1):
                res+='a'
            if(i<len(a)-1):
                res+=' '
        return res
                    