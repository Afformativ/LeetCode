class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

#Second Solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n:
            ans+=n & 1
            n>>=1
        return ans
