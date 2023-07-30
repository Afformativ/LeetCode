class Solution:
    def numberOfMatches(self, n: int) -> int:
        res=0
        while n>=2:
            matches=n//2
            res+=matches
            n=n//2 if n%2==0 else (n//2+1)
        return res
