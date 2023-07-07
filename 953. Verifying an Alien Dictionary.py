class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)<2:
            return True
        d={l:i for i,l in enumerate(order)}
        d['#']=-1
        for i in range(1,len(words)):
            w1=words[i-1]
            l1=len(w1)
            w2=words[i]
            l2=len(w2)

            if l1<l2:
                w1+='#'*(l2-l1)
            else:
                w2+='#'*(l1-l2)
            for j in range(l1):
                if d[w1[j]]<d[w2[j]]:
                    break
                if d[w1[j]]>d[w2[j]]:
                    return False
        return True
