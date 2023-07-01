class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid=len(nums)//2
        low=0
        high=len(nums)-1
        while nums[mid] != target and low<= high:
            if target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
            mid=(low+high)//2
        if low > high:
            return low
        else:
            return mid
#Second solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target)
