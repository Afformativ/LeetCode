class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i]==0:
                    continue
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        return nums
#Second Solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,mid,r=0,0,len(nums)-1
        for i in range(len(nums)):
            if nums[mid]==0:
                nums[l],nums[mid]=nums[mid],nums[l]
                l+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[r]=nums[r],nums[mid]
                r-=1
