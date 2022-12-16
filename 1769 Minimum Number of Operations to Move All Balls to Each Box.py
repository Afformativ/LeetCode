class Solution(object):
    def minOperations(self, boxes):
        boxes=list(boxes)
        counter=0
        res=[]
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    counter = counter +abs(i - j)
            res.append(counter)
            counter=0
        return res
