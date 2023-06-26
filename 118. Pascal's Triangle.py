class Solution:
    def generate(self, n: int) -> List[List[int]]:        
        def helper(n):
            if n:
                helper(n-1)                
                ans.append([1]*n)          
                for i in range(1, n-1):     
                    ans[n-1][i] = ans[n-2][i] + ans[n-2][i-1]
        ans = []
        helper(n)
        return ans

#Second solution
class Solution:
    def generate(self, n: int) -> List[List[int]]:        
        dp=[[1],[1,1]]

        if n <3:
            return dp[:n]

        
        for _ in range(n-2):
            next_row=[1]
            for i in range(1,len(dp[-1])):
                next_row.append(dp[-1][i]+dp[-1][i-1])

            next_row+=[1]
            dp.append(next_row)
        return dp
