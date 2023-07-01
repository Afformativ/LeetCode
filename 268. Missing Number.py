class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(max(nums)):
            if i not in nums:
                return i
        return max(nums)+1
#Second Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(len(nums)+1))-set(nums))[0]
