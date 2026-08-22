class Solution {
public:
    bool checkDivisibility(int n) {
        int sum=0;
        int prod=1;
        int rem;
        int m=n;
        while(n>0){
            rem=n%10;
            sum+=rem;
            prod*=rem;
            n/=10;
        }
        return m%(sum+prod)==0;
    }
};