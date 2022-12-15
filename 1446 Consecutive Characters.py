class Solution(object):
    def maxPower(self, s):
        s.split()
        counter=1
        power=0      
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                counter+=1
            else:
                power=max(power,counter)
                counter=1
        power = max(power, counter)
        return power

