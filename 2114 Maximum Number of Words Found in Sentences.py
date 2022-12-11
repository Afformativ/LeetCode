class Solution(object):
    def mostWordsFound(self, sentences):
        count=[]
        for i in sentences:
            a=i.split()
            count.append(len(a))
        max=count[len(count)-1]
        for i in range(len(count)):
            if max< count[i]:
                max=count[i]
        return max
