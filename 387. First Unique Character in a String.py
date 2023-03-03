class Solution:
    def firstUniqChar(self, s: str) -> int:
        k=set(s)
        arr=[]
        for i in k:
            if s.count(i)==1:
                arr.append(s.index(i))
        return min(arr) if arr else -1
