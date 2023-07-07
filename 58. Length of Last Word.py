class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l=s.split(' ')
        return len(l[-1])


#Second Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur=0
        prev=None
        for c in s:
            if c==' ':
                if prev!=' ':
                    last=cur
                    cur=0
            else:
                cur+=1
            prev=c
        return last if not cur else cur
#Third Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=''
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                if word:
                    return len(word)
            else:
                word+=s[i]
        return len(word)
