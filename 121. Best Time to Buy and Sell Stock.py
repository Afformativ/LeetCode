class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_,max_=float(inf),0
        for i in prices:
            if i<min_:
                min_=i
            else:
                max_=max(max_,i-min_)
        return max_
