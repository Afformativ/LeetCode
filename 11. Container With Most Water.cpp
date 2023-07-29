class Solution {
public:
    int maxArea(vector<int>& height) {
        vector<int> ans;
        int l=0,r=height.size()-1;
        while (l<=r){
            if (height[l]>height[r]){
                ans.push_back(height[r]*(r-l));
                r-=1;
            }
            else{
                ans.push_back(height[l]*(r-l));
                l+=1;
            }
        }
        return *max_element(ans.begin(), ans.end());
    }
};
