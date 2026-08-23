class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int count=0;
        int temp=capacity;
        for(int i=0;i<plants.size();i++){
            if(plants[i]>temp){
                count+=i*2;
                temp=capacity;
            }
            count++;
            temp-=plants[i];
        }
        return count;
    }
};