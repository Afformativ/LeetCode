def average(sum_:int, count:int)->int:
    return sum_ // count if count else 0

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        min_avg_diff,argmin=math.inf,-1
        pref_sum=list(itertools.accumulate(nums))

        for i in range(n):
            pref_avg=average(pref_sum[i],i+1)
            suff_avg=average(pref_sum[-1]-pref_sum[i],n-i-1)

            avg_diff=abs(pref_avg-suff_avg)
            if min_avg_diff>avg_diff:
                min_avg_diff,argmin=avg_diff,i

        return argmin
      
      
