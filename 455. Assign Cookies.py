class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans=0
        i=0
        for c in s:
            if c>=g[i]:
                ans+=1
                i+=1
            if i == len(g):
                break
        return ans
