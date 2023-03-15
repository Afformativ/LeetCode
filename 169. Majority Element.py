class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        s=set(nums)
        for i in s:
            dic[i]=nums.count(i)
        key_list = list(dic.keys())
        val_list = list(dic.values())
        return key_list[val_list.index(max(val_list))]
