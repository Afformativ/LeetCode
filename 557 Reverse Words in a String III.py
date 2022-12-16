class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        res=[]
        for i in s:
            k=list(i)
            j=''.join(reversed(k))
            res.append(j)
        return ' '.join(res)
