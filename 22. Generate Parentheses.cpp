class Solution {
public:
    vector <string> result;
    string current;
    void generate(int index, int len, int delta){
        if (delta<0){
            return;
        }
        if (index==len){
            if (delta==0){
                result.push_back(current);
            }
            return;
        }

        current.push_back('(');
        generate(index+1,len,delta+1);
        current.pop_back();

        current.push_back(')');
        generate(index+1,len,delta-1);
        current.pop_back();

    };
    vector<string> generateParenthesis(int n) {
        generate(0,n+n,0);
        return result;
    }
};
