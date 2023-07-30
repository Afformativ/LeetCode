class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        counter=0
        for i in range(len(hours)):
            if hours[i]>=target:
                counter+=1
        return counter
