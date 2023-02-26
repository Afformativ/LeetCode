class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return res
