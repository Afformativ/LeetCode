class Solution:
    def longestPalindrome(self, s: str) -> int:
        u=set(s)
        d={}
        res=0
        m=0
        for i in u:
            d[i]=s.count(i)
        for v in d.values():
            if v%2==0:
                res+=v
            else:
                res=res+v-1
                m=1
        return res+m
#Second Solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt=Counter(s)

        ans=0
        
        for l,c in cnt.items():
            cur=c-(c%2)
            ans+=cur
            cnt[l]-=cur

        return ans if not sum(cnt.values()) else ans +1
