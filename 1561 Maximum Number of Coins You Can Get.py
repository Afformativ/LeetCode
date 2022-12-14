class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        count=0
        r=len(piles)//3
        for i in range(1,len(piles),2):
            count+=piles[i]
            r-=1
            if r ==0:
                break
              
        return count
