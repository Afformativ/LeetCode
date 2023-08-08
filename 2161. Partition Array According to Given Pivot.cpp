class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> smaller,same,greater;
        for(int i=0;i<nums.size();++i){
            if(nums[i]<pivot){
                smaller.push_back(nums[i]);
            }
            else if (nums[i]>pivot){
                greater.push_back(nums[i]);
            }
            else{
                same.push_back(nums[i]);
            }
        }
        smaller.insert( smaller.end(), same.begin(), same.end() );
        smaller.insert( smaller.end(), greater.begin(), greater.end() );
        return smaller;
    }
};
