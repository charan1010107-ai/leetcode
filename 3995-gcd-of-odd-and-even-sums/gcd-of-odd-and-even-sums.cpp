class Solution {
public:
    int gcdOfOddEvenSums(int n) {
        long long esum=0;
        int ec=0,oc=0;
        long long osum=0;
        for(int i=2;ec<n;i+=2){
            esum+=i;
            ec++;
        }for(int i=1;oc<n;i+=2){
                osum+=i;
                oc++;
        }
        return gcd(osum,esum);
    }
};