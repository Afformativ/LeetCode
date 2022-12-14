class Solution(object):
    def convertTime(self, current, correct):
        cur=current.split(":")
        cor=correct.split(":")
        res=int(cor[0])-int(cur[0])
        b=int(cor[1])-int(cur[1])
        if b<0:
            res-=1
            b=60-int(cur[1])+int(cor[1])
        while b>=15:
           b-=15
           res+=1
        while b>=5:
            b-=5
            res+=1
        while b>=1:
            b-=1
            res+=1
        return res

