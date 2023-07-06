class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        n=len(nums)
        l=0
        cur=0
        for r in range(n):
            cur+=nums[r]
            
            while cur>=target:
                cur-=nums[l]
                ans=min(ans,r-l+1)
                l+=1
        if ans ==float('inf'):
            return 0
        return ans
