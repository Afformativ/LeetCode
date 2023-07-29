class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=[]
        l,r=0,len(height)-1
        while l<=r:
            if height[l]>height[r]:
                ans.append(height[r]*(r-l))
                r-=1
            else:
                ans.append(height[l]*(r-l))
                l+=1
        return max(ans)
