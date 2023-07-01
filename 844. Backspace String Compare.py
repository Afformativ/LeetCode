class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stack2=[]
        for c in s:

            if c=='#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        for c in t:
            if c=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(c)
        return ''.join(stack)==''.join(stack2)


#Second Solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typing(s):
            stack=[]
            for c in s:
                if c=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        return typing(s)==typing(t)
