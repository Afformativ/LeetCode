class Solution(object):
    def findGCD(self, nums):
        minimum=min(nums)
        maximum=max(nums)
        res=0
        for i in range(1,min(minimum,maximum)+1):
            if minimum%i==0 and maximum%i==0:
                res=i
        return res
