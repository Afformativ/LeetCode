class Solution:
    def minimumSum(self, num: int) -> int:
        x = [a for a in str(num)]
        x.sort()
        new1=x[0]+x[2]
        new2=x[1]+x[3]
        return int(new1)+int(new2)
