class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        unordered_map<int, int> myMap;
        for(int num:nums)
        {
            if(myMap.find(num) != myMap.end())
                return true;
            else
                myMap.insert({num, 1});
        }
        return false;
    }
};
