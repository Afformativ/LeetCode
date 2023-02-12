class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concut=[]
        for i in range(len(nums)//2):
            k=int(str(nums[i])+str(nums[len(nums)-1-i]))
            concut.append(k)
        if (len(nums))%2==1:
            concut.append(nums[len(nums)//2])
        return sum(concut)
        
