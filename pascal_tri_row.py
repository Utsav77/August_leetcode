class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[]
        p=1
        a.append(p)
        for i in range(1,rowIndex+1):
            c=(p*(rowIndex-i+1))//i
            a.append(c)
            p=c
        return a