class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            sup=nums[l[i]:r[i]+1]
            sup=sorted(sup)
            differences = [sup[i+1] - sup[i] for i in range(len(sup) - 1)]
            k=set(differences)
            if len(k)>1:
                res.append(False)
            else:
                res.append(True)
        return res
