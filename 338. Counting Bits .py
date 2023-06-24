class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            k=format(i,'b')
            if int(k)>9:
                res.append(k.count("1"))
            else:
                res.append(int(k))
        return res

#Second Solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]
        for i in range(1,n+1):
            cur=0
            while i:
                cur+=i&1
                i >>=1
            ans.append(cur)

        return ans
