class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        summ=0
        res=0
        for i in range(len(satisfaction)):
            summ+=satisfaction[i]
            if summ <0:
                break
            res+=summ
        return res

