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
        
