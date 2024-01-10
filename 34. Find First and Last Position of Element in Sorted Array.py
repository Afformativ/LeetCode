class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        res=[-1,-1]
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                lt=rt=mid
                while lt>=0 and nums[lt]==target:
                    res[0]=lt
                    lt-=1
                while rt<=r and nums[rt]==target:
                    res[1]=rt
                    rt+=1
                return res
            else:
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
        return res
        
