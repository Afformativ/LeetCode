class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=[]
        res=0
        for i in range(len(bank)):
            k=0
            for j in range(len(bank[i])):
               k+=int(bank[i][j])
            if k>0:
                ans.append(k)
        for i in range(len(ans)-1):
            res+=ans[i]*ans[i+1]
        return res
