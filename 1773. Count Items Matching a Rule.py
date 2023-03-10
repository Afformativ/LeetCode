class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer=0
        id=2

        if ruleKey=='type':id=0
        elif ruleKey=='color':id=1

        for i in items:
            if i[id] == ruleValue: answer+=1
        return answer
