class Solution(object):
    def countPoints(self, points, queries):
        counter=0
        res=[]
        for i in queries:
            for j in points:
                r=(j[0]-i[0])**2+(j[1]-i[1])**2
                if r<=(i[2]**2):
                    counter+=1
            res.append(counter)
            counter=0
        return res
