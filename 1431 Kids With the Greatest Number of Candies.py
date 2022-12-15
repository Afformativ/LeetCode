class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        r=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=r:
                res.append(True)
            else:
                res.append(False)
        return res
