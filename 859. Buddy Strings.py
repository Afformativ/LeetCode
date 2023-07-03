class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)< len(goal):
            return False
        if s==goal and len(set(s))<len(s):
            return True
        counter=0
        for i in range(len(s)):
            if s.count(s[i])!=goal.count(s[i]):
                return False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                counter+=1
        print(set(s)==set(goal))
        if counter==2:
            return True
        else:
            return False
