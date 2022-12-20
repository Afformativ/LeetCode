class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        r, res = x, 0
        while r:
            res = res * 10 + r % 10
            r /= 10
        return res == x
