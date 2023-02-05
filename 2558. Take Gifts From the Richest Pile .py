import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            idx=gifts.index(max(gifts))
            gifts[idx]= int(math.sqrt(gifts[idx]))
        return sum(gifts)
