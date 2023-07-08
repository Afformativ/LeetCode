class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in jewels:
            for j in stones:
                if i==j:
                    count+=1
        return count
#Second Solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels =set(jewels)
        ans=0
        for s in stones:
            if s in jewels:
                ans+=1
        return ans
