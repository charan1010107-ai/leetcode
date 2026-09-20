class Solution {
public:
    int reverseDegree(string s) {
        int sum=0;
        for(int i=0;i<s.length();i++){
            char ch=s[i];
            int x=abs(26-(ch-97));
            sum+=((i+1)*x);
        }
        return sum;
    }
};