class Solution:
    def firstUniqChar(self, s: str) -> int:
        k=set(s)
        arr=[]
        for i in k:
            if s.count(i)==1:
                arr.append(s.index(i))
        return min(arr) if arr else -1

#Second Solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt=Counter(s)
        for i,c in enumerate(s):
            if cnt[c]==1:
                return i
        return -1
