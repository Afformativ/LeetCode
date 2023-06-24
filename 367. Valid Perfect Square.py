class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        low=1
        high=num//2
        while low<=high:
            mid=(low+high)//2
            sq=mid*mid
            if sq <num:
                low=mid+1
            elif sq >num:
                high=mid-1
            else:
                return True
        return False
