class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return(sum(set(nums))*2-sum(nums))

#Second solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0

        for num in nums:
            ans^=num
        return ans
