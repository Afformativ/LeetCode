class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l=list(s)
        count=0
        for i in range(len(l)//2):
            if l[i] in vow:
                count+=1
        for i in range(len(l)//2,len(l)):
            if l[i] in vow:
                count-=1
        return True if count==0 else False
