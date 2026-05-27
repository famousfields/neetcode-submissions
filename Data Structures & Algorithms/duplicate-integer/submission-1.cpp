class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        unordered_set <int> mySet;

        for(int num:nums)
        {
            mySet.insert(num);
        }
        return  mySet.size() == nums.size() ? false : true;
    }
};