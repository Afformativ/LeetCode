class Solution {
public:
    int numberOfMatches(int n) {
        int res=0;
        while(n>=2){
            int matches=n/2;
            res+=matches;
            if (n%2==0){
                n/=2;
            }
            else{
                n=n/2+1;
            }
        }
        return res;
    }
};
