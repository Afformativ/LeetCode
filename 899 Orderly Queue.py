class Solution(object):
    def orderlyQueue(self, s, k):
        if k>1:
            return ''.join(sorted(s))
        else:
            ans=s
            for i in range(1,len(s)):
                ans=min(ans,s[i:]+s[:i])
            return ans
