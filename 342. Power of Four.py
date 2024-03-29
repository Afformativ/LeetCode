class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        while n%4==0:
            n=n//4
        if n==1:
            return True
        else:
            return False


#Second solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True

        return self.isPowerOfFour(n/4)
