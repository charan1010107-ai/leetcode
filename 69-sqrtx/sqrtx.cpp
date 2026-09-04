class Solution {
public:
    int mySqrt(int x) {
        int count=0;
        for(int i=1;x>=i;i+=2){
            x-=i;
            count++;
        }
        return count;
    }
};