class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        counter=0
        for j in ['P','G','M']:
            if j in garbage[len(garbage)-1]:
                for t in range(len(garbage)-1):
                    counter+=travel[t]
            else:
                for i in range(len(garbage)-1,0,-1):
                    if j in garbage[i]:
                        for t in range(i):
                            counter+=travel[t]
                        break
                    
        for i in range(len(garbage)):
            counter+=len(garbage[i])
        
        return counter
