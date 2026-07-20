class Solution {
public:
    int scoreOfString(string s) {
        vector<int> a;
        vector<int> b;
        int sum=0;
        for(int i=0;i<s.length();i++){
            char ch=s[i];
            int x=int(ch);
            a.push_back(x);
        }
        for(int i=0;i<a.size()-1;i++){
            int p=abs(a[i]-a[i+1]);
            b.push_back(p);
        }
        for(int i=0;i<b.size();i++){
            sum+=b[i];
        }
        return sum;
    }
};