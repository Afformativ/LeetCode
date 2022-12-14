class Solution(object):
    def minOperations(self, n):
        count=0
        for i in range(1,n,2):
            count=count+(n-i)
        return count

    class Solution(object):
    def minOperations(self, n):
        return (n//2)*((n+1)//2)
