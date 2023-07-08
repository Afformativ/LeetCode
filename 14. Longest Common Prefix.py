class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]

        ans=''
        i=0
        for i in range(len(first)):
            flag=True
            for word in strs[1:]:
                if i>len(word)-1 or first[i] != word[i]:
                    flag=False
                    break
            if flag:
                ans+=first[i]
            else:
                break
        return ans
