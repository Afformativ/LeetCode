class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set()
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in seen:
                seen.add(nums1[i])
                res.append(nums1[i]) 
        return res


#Second Solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=Counter(nums1)
        c2=Counter(nums2)
        return c1 & c2
