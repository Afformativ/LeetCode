class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums+=[0]
        ans=[]
        l=0
        for i in range(len(nums)):
            if nums[i]==0:
                ans.append(sum(nums[l:i]))
                l=i
        return max(ans)


#Second Solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp=[0]*(len(nums)+1)

        for i in range(len(nums)):
            if nums[i]:
                dp[i+1]=dp[i]+1
            else:
                dp[i+1]=0
        return max(dp)
