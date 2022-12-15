class Solution(object):
    def dayOfYear(self, date):
        res=date.split('-')
        m=res[1]
        ans=0
        day=[0,31,59,90,120,151,181,212,243,273,304,334]
        if int(res[0])%4==0 and int(m)>2 and int(res[0])!=1900:
            ans+=1
        ans=ans+int(day[int(m)-1])+int(res[2])
        return ans
