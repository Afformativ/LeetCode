class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even+odd


#Second Solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        return nums
