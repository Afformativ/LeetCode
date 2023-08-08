class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        same=[]
        greater=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                small.append(nums[i])
            elif nums[i]==pivot:
                same.append(nums[i])
            else:
                greater.append(nums[i])
        return small+same+greater
