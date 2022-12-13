class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum=0
        x=[int(a) for a in str(n)]
        for i in x:
            prod*=i
            sum+=i
        return prod-sum
