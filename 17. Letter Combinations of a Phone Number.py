class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        comb={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        ans=[]

        def backtracking(combination,next_digits):
            if not next_digits:
                ans.append(combination)
                return
            for el in comb[next_digits[0]]:
                backtracking(combination+el,next_digits[1:])
        backtracking('',digits)
        return ans
