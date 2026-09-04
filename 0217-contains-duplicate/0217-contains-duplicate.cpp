class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> x(nums.begin(),nums.end());
        if (nums.size()!=x.size()){
            return true;
        }else{
            return false;
        }
    }
};