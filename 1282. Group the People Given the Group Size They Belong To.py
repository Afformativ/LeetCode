class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        s=set(groupSizes)
        s=sorted(s)
        res=[]
        sup=[]
        for i in s:
            for j in range(len(groupSizes)):
                if groupSizes[j]==i:
                    sup.append(j)
                if len(sup)==i:
                    res.append(sup[:])
                    sup.clear()
        return res
