class Solution(object):
    def commonFactors(self, a, b):
        counter=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                counter+=1
        return counter
