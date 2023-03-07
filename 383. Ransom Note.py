class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        k=list(magazine)
        for i in ransomNote:
            if i in k:
                k.remove(i)
            else:
                return False
        return True
            
