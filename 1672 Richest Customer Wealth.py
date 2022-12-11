class Solution(object):
    def maximumWealth(self, accounts):
        count=[]
        cnt=0
        for i in accounts:
            for el in i:
                cnt+=el
            count.append(cnt)
            cnt=0
        max=count[len(count)-1]
        for i in range(len(count)):
            if max< count[i]:
                max=count[i]
        return max
