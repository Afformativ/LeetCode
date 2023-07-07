class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        m=max(arr)
        a=arr.index(m)
        if a==0 or a==len(arr)-1:
            return False
        for i in range(a):
            if arr[i]>=arr[i+1]:
                return False
        for i in range(a,len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False
        return True


#Second Solution
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i=0
        while i<len(arr)-1 and arr[i]<arr[i+1]:
            i+=1
        j=len(arr)-1
        while j>0 and arr[j-1]>arr[j]:
            j-=1
        return i==j and 0<i<len(arr)-1
