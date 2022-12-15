class Solution(object):
    def restoreString(self, s, indices):
        res=[0]*len(s)
        for i in range(len(s)):
            for j in range(i,len(s)):
                res[indices[j]]=s[i]
                break
        return ''.join(res)
