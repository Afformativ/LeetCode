class Solution(object):
    def addDigits(self, num):
        return num%9 or num and 9
