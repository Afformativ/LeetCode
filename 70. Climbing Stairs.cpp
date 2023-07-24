class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+2,0);

        dp[0]=1;
        for(int i=0;i<n;++i){
            int cur=dp[i];
            dp[i+1]+=cur;
            dp[i+2]+=cur;
        }
        return dp[n];
    }
};
