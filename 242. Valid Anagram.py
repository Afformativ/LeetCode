# solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t=list(t)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        return True
      
 #solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in s:
            if s.count(i)!=t.count(i):
                return False
        return True
