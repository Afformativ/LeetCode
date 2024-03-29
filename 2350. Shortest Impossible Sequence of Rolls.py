class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 0 
        seen = set()
        for x in rolls: 
            seen.add(x)
            if len(seen) == k: 
                ans += 1
                seen.clear()
        return ans+1
