class Solution(object):
    def largestOddNumber(self, num):
        arr=list(num)
        for i in reversed(range(len(arr))):
            if int(arr[i])%2==1:
                break
            else:
                del(arr[i])
        return ''.join(arr)
