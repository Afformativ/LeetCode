class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        prefix = 0
        for i in range(len(word)):
            prefix = (prefix * 10 + int(word[i])) % m
            if prefix == 0:
                res[i] = 1
        return res
        
