class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)
        while l< r:
            mid=(l+r)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            if arr[mid]<arr[mid+1]:
                l=mid+1
            else:
                r=mid
        return l
            
