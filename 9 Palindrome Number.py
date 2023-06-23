class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        r, res = x, 0
        while r:
            res = res * 10 + r % 10
            r /= 10
        return res == x

#Second solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0:] == str(x)[::-1]:
            return True
        return False 

#Third solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False

        new=0
        orig=x

        while x:
            x,d=divmod(x,10)
            new=new*10+d

        return new==orig
            
