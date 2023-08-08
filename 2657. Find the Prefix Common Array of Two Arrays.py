class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen=set()
        res=[]
        d=0
        for i in range(len(A)):
            count=0
            if A[i] in seen:
                count+=1
            seen.add(A[i])
            if B[i] in seen:
                count+=1
            if i>0:
                res.append(res[i-1]+count)
            else:
                res.append(count)
            seen.add(B[i])
        return res
