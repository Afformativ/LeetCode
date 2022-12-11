class Solution(object):
    def minPartitions(self, n):
        res=0
        for i in n:
            res=max(res,int(i))
        return res
            
