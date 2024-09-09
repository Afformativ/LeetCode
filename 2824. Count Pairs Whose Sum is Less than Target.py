class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])<target:
                    cnt+=1
        return cnt
//Second Solution with Binary search
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res=0
        for i,n in enumerate(nums):
            value=target-n
            res+=self.binSearch(i+1,value,nums)
        return res

    def binSearch(self,start,value,nums):
        l,h=start,len(nums)
        while l<h:
            mid=(l+h)//2
            if nums[mid]< value:
                l=mid+1
            else:
                h=mid
        return l-start

        
