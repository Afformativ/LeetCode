class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        summ=0
        if k>numOnes:
            summ+=numOnes
            k-=numOnes
            if k>numZeros:
                k-=numZeros
                return summ-k
            else:
                return summ
        else:
            return k
