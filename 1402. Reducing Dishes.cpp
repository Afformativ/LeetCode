class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end(), greater<int>());
        int sum=0,res=0;
        for (int i=0;i<satisfaction.size();++i){
            sum+=satisfaction[i];
            if(sum<0){
                break;
            }
            res+=sum;
        }
        return res;
    }
};
