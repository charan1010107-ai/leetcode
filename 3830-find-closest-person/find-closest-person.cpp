class Solution {
public:
    int findClosest(int x, int y, int z) {
        int xsp,ysp;
        xsp=abs(z-x);
        ysp=abs(z-y);
        if(xsp>ysp){
            return 2;
        }else if(ysp>xsp){
            return 1;
        }else{
            return 0;
        }
    }
};