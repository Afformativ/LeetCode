class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=abs(x)
            x=str(x)
            x=x[::-1]
            x=int(x)
            if x < -2**31 or x > 2**31 - 1:
                return 0
            else:
                return -x
        else:
            x=str(x)
            x=x[::-1]
            x=int(x)
            if x < -2**31 or x > 2**31 - 1:
                return 0
            else:
                return x
#Second Solution
class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        nums=list(str(x))
        l,r=0,len(nums)-1
        res=[]
        while nums[r]=='0':
            r-=1
        while l<=r:
            if nums[l]=='-':
                res.append(nums[l])
                l+=1
            else:
                res.append(nums[r])
                r-=1
        k=int(''.join(res)) 
        if k>2 ** 31 - 1 or k<-2 ** 31:
            return 0
        else:
            return k
