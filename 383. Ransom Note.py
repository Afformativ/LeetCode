class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        k=list(magazine)
        for i in ransomNote:
            if i in k:
                k.remove(i)
            else:
                return False
        return True
            
#Second Solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_r=Counter(ransomNote)
        cnt_m=Counter(magazine)
        return (cnt_r & cnt_m) == cnt_r
