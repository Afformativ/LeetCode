class Solution(object):
    def countDistinctIntegers(self, nums):
        res=[]
        n2=0
        for i in nums:
            res.append(i)
        for i in nums:
           n2 = str(i)[::-1]
           res.append(int(n2))
        return len(set(res))
