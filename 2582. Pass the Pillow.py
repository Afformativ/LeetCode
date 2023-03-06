class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1  
        current_person = 1
        for i in range(time):
            if current_person == n:
                direction = -1
            elif current_person == 1:
                direction = 1
            current_person += direction
        return current_person
        
