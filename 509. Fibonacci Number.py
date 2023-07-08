class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        return self.fib(n-1) + self.fib(n-2)


#Second Solution
class Solution:
  def fib(self, n: int) -> int:
    if n < 2:
      return n

    dp = [0, 0, 1]

    for i in range(2, n + 1):
      dp[0] = dp[1]
      dp[1] = dp[2]
      dp[2] = dp[0] + dp[1]

    return dp[2]
