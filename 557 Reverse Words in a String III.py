class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        res=[]
        for i in s:
            k=list(i)
            j=''.join(reversed(k))
            res.append(j)
        return ' '.join(res)

#Second Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')

        for i in range(len(s)):
            s[i]=s[i][::-1]

        return ' '.join(s)
