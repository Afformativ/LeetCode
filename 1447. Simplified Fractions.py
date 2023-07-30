class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans=[]
        res=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                if (i!=1 and j%i==0) or i/j in res:
                    continue
                if i/j not in res:
                    res.append(i/j)
                
                ans.append(str(i)+'/'+str(j))
        return ans


#Second Solution
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        seen={}
        ans=[]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i/j not in seen:
                    seen[i/j]=1
                    ans.append(f"{i}/{j}")
        return ans
