class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        seen=set()
        answer=[]

        for word in words:
            m=len(word)
            partition=[True]+[False]*m

            for r in range(1,m+1):
                for l in range(r):
                    if partition[l] and word[l:r] in seen:
                        partition[r]=True
            if partition[m]:
                answer.append(word)
            seen.add(word)
        return answer
