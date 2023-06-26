class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=2,x//2
        if x<2:
            return x
        while low<=high:
            mid=(low+high)//2
            sq=mid*mid
            if sq>x:
                high=mid-1
            else:
                low=mid+1 
        return high
