class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter=0
        answer=0
        for i in range(len(s)):
            if s[i]=='R':counter+=1
            else:counter-=1
            if counter==0:answer+=1
        return answer
