class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        def binary_search(val):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= val:
                    left = mid + 1
                else:
                    right = mid
            return left

        ans = []
        for i in queries:
            index = binary_search(i)
            neg_sum = index * i - prefix_sum[index]
            pos_sum = prefix_sum[-1] - prefix_sum[index] - (len(nums) - index) * i
            ans.append(pos_sum + neg_sum)

        return ans
