class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        return count
//Second solution with bionary search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        for ins in grid:
            res+=self.binSearch(ins)
        return res
        
    def binSearch(self,arr):
        l,h=0,len(arr)-1
        while l<=h:
            mid = (l+h)//2
            if arr[mid] < 0:
                h=mid-1
            else:
                l=mid+1
        return len(arr)-l
            
        
