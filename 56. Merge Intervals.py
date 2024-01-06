class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output=[]
        intervals=sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]: 
                intervals[i+1][0]=intervals[i][0]
                intervals[i+1][1]=max(intervals[i][1],intervals[i+1][1])
        for j in range(len(intervals)-1):
            if intervals[j][0]!=intervals[j+1][0]:
                output.append(intervals[j])
        output.append(intervals[-1])
        intervals=output
        return intervals
