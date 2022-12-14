class Solution(object):
    def largestGoodInteger(self, num):
        arr=list(num)
        res=[]
        for i in range(1,len(arr)-1):
            if arr[i-1]==arr[i] and arr[i]==arr[i+1]:
                res.append(arr[i])
        if len(res)==0:
            return ""
        b=max(res)
        result=[b]*3
        return "".join(result)
