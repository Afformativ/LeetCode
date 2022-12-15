class Solution(object):
    def reverseString(self, s):
        start=0
        finish=len(s)-1
        while start<finish:
            t=s[start]
            s[start]=s[finish]
            s[finish]=t
            start+=1
            finish-=1
        return s
