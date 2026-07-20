class Solution {
public:
    int sumOfMultiples(int n) {
        vector<int> b;
        int sum=0;
        for(int i=1;i<=n;i++){
            if(i%3==0||i%5==0||i%7==0){
                b.push_back(i);
            }
        }
        for(int i=0;i<b.size();i++){
            sum+=b[i];
        }
        return sum;
    }
};