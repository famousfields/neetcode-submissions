class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        if(s.size()!=t.size())
            return false;
        vector<int> charCount(26,0);

        for(char c:s)
        {
            charCount[c-'a']++;
        }
        for(char c:t)
        {
            charCount[c-'a']--;
        }
        for(int c:charCount)
        {
            if(c != 0)
                return false;
        }
        return true;
    }
};
