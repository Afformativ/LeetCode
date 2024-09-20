class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums2:
            if i in nums1:
                nums1.remove(i)
                res.append(i)
        return res
#Second Solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        l=r=0
        while l<len(nums1) and r<len(nums2):
            if nums1[l]==nums2[r]:
                res.append(nums1[l])
                l+=1
                r+=1
            elif nums1[l]>nums2[r]:
                r+=1
            else:
                l+=1
        return res
