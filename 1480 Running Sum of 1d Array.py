class Solution(object):
    def runningSum(self, nums):
        #a=[0]*len(nums)
        #a[0]=nums[0]
        a=[]
        a.append(nums[0])
        for i in range(1,len(nums)):
            a.append(nums[i]+a[i-1])
        return a

#Second Solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
