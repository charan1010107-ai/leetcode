class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> res;
        vector<int>p;
        vector<int>q;
        for(int i=0;i<nums.size();i++){
            if(nums[i]>0){
                p.push_back(nums[i]);
            }else{
                q.push_back(nums[i]);
            }
        }
        for(int i=0;i<p.size();i++){
            res.push_back(p[i]);
            res.push_back(q[i]);
        }
        return res;
    }
};