class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        q=deque([])
        ans=-float('inf')
        cnt=0
        cur=0
        for i in range(len(nums)):
            cur+=nums[i]
            cnt+=1
            if cnt==k:
                ans=max(ans,cur/k)
            if cnt >k:
                cur-=nums[i-k]
                ans=max(ans,cur/k)
        return ans
