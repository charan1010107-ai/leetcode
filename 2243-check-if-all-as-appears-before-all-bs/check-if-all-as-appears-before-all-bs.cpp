class Solution {
public:
    bool checkString(string s) {
        int count=0;
        if(s[0]=='a'){
        for(int i=0;i<s.size()-1;i++){
            if(s[i]!=s[i+1]){
                count++;
            }
        }
        if(count<=1){
            return true;
        }else{
            return false;
        }
        }else{
            for(int i=0;i<s.size()-1;i++){
            if(s[i]!=s[i+1]){
                count++;
            }
            }
            if(count==0){
            return true;
        }else{
            return false;
        }
        }
    }
};