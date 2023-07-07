class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        s=set(nums)
        for i in s:
            dic[i]=nums.count(i)
        key_list = list(dic.keys())
        val_list = list(dic.values())
        return key_list[val_list.index(max(val_list))]

#Second Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

#Third Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None

        for num in nums:
            if count==0:
                candidate=num
            count+=(1 if num==candidate else -1)
        return candidate
