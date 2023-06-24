class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        arr=coordinates
        x=coordinates[0][0]
        y=coordinates[0][1]

        for i in range(1,len(coordinates)-1):
            if (x-arr[i][0])*(arr[i+1][1]-arr[i][1])!=(arr[i+1][0]-arr[i][0])*(y-arr[i][1]):
                return False
        return True
