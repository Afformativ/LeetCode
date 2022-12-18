class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        left=ans=counter=0
        string=list(s)
        curr=[]
        for right in range(len(string)-1):
            curr.append(string[right])
            while string[right+1] in curr:
                del curr[left]
                counter+=1
            ans=max(ans,right-counter+2)
        return ans
