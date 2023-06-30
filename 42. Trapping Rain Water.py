class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[0]*len(height)
        max_right=[0]*len(height)
        ans=0
        for i in range(1,len(height)):
            max_left[i]=max(height[i-1],max_left[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i+1])
        for i in  range(len(height)):
            water=min(max_right[i],max_left[i])
            if water>height[i]:
                ans+=(water-height[i])
            
        return ans
