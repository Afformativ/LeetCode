class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        res=nums[0]+nums[1]+nums[2]
        if res==target:
            return res
        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            while j<k:
                cur=nums[i]+nums[j]+nums[k]
                if abs(cur-target)<abs(res-target):
                    res=cur
                if cur > target:
                    k-=1
                elif cur<target:
                    j+=1
                else:
                    return res
        return res
