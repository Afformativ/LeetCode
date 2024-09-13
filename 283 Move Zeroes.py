class Solution(object):
    def moveZeroes(self, nums):
        k=nums.count(0)
        counter=0
        while k>0:
            nums.remove(0)
            k=nums.count(0)
            counter+=1
        for i in range(counter):
            nums.append(0)
        return nums

#Second Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
#Third Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,1
        while l<len(nums) and r<len(nums):
            if nums[l]!=0:
                l+=1
                r+=1
            elif nums[l]==0:
                while r<len(nums) and nums[r]==0 :
                    r+=1
                if r<len(nums):
                    temp=nums[l]
                    nums[l]=nums[r]
                    nums[r]=temp
                    l+=1
                    r+=1


