class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t=list(t)
        for i in s:
            if i in t:
                t.remove(i)
        return t[0]

  #Second Solution
  class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i
