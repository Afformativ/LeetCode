class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res=int(''.join(map(str, num)))
        d=int(res)+k
        ans=[]
        d=list(str(d))
        for i in d:
            ans.append(int(i))
        return ans
