class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = len(nums)
        ans = []
        present = [False] * (m + 1)  # 1-based indexing
        for num in nums:
            present[num] = True
        for i in range(1, m + 1):
            if not present[i]:
                ans.append(i)
        return ans


#Second Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1,len(nums)+1)) -set(nums)
