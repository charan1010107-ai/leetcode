class Solution {
public:
    string toLowerCase(string s) {
        string res="";
        for(int i=0;i<s.length();i++){
            char ch=s[i];
            if(ch>='A'&&ch<='Z'){
                res+=ch+32;
            }else{
                res+=ch;
            }
        }
        return res;
    }
};