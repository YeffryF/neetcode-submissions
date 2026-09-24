class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int curr_max = 0;
        int curr = 0;
        for(int i = 0; i < nums.size(); i++) {
           if(nums[i] == 1) {
            curr++;
            curr_max = std::max(curr_max, curr);
           } else {
            curr = 0;
           }
        }
        return curr_max;
    }
};