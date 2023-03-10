#First
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
      
#Second
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=''

        for i in range(len(s)):
            idx=ord(s[i])
            if idx >= 65 and idx <=90: idx+=32
            ans+=chr(idx)
        return ans
