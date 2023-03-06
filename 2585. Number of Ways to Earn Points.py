MOD = 10**9 + 7

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            counti, marksi = types[i-1]
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                for k in range(1, counti+1):
                    if k*marksi <= j:
                        dp[i][j] += dp[i-1][j-k*marksi]
                        dp[i][j] %= MOD
        return dp[n][target]
        
