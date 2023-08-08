class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr=[i for i in range(1,m+1)]
        res=[]
        for i in range(len(queries)):
            k=queries[i]
            b=arr.index(k)
            res.append(b)
            arr.remove(k)
            arr.insert(0,k) 
        return res
