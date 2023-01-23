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

    
    #Second solution
def count_vowels(s:str)->int:
    return sum(c.lower() in 'aeiou' for c in s)


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = len(s) // 2
        a, b=s[:m], s[m:]
        return count_vowels(a)==count_vowels(b)
