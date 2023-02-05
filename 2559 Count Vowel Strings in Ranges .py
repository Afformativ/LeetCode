class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels=['a','e','o','u','i']
        ans=[]
        supp=[0]*(len(words)+1)
        
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                supp[i+1]=supp[i]+1
            else:
                supp[i+1]=supp[i]
                
        for j in queries:
            l,r=j
            ans.append(supp[r+1]-supp[l])
        return ans
            
