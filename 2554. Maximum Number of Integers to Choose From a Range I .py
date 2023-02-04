class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        counter=0
        summ=0
        arr = set(banned)
        
        for i in range(1,n+1):
            if i not in arr and (i+summ)<=maxSum:
                summ+=i
                counter+=1
            
        return counter
