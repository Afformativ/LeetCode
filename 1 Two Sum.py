class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]

#Second Solution
class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[(target-nums[i])]=i
            else:
                return[i,d[nums[i]]]
#Third Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                res.append(i)
                for j in range(i+1,len(nums)):
                    if (target-nums[i])==nums[j]:
                        res.append(j)
                return res
