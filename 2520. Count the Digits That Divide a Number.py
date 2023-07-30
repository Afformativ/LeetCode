class Solution:
    def countDigits(self, num: int) -> int:
        n=list(str(num))
        cnt=0
        for i in n:
            if num%int(i)==0:
                cnt+=1
        return cnt
