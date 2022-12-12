from math import gcd
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = nums[0]
        for i in nums:    
            x = gcd(x, i) 
        return x == 1
