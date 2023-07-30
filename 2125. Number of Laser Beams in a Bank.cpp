class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        vector<int> ans;
        int res=0;
        for(int i=0;i<bank.size();++i){
            int k=0;
            for(int j=0;j<bank[i].size();++j){
                if(bank[i][j]=='1'){
                    k+=1;
                }
            }
            if(k>0){
                ans.push_back(k);
            }
        }
        if(ans.size()<=1){  
            return 0;
        }
        for(int el=0;el<ans.size()-1;++el){
            res+=ans[el]*ans[el+1];
        }
        return res;
    }
};
