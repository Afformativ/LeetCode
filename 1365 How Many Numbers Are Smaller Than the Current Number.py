class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count=0
        res=[]
        for j in nums:
            for i in nums:
                if j>i:
                    count+=1
            res.append(count)
            count=0
        return res
