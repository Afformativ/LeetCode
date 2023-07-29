class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def helper(amount):
            if amount == 0:
                return 0
            if amount<0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            ret=float('inf')

            for c in coins:
                ret=min(ret,1+helper(amount-c))
            memo[amount]=ret
            return ret
        ans = helper(amount)
        return ans if ans!=float('inf') else -1


#Second Solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1,len(dp)):
            for c in coins:
                if c<=i:
                    dp[i]=min(dp[i],1+dp[i-c])

        return dp[-1] if dp[-1] != float('inf') else -1
