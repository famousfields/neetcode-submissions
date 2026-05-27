class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        if(s.size() != t.size())
            return false;

        string temp1 = s, tmp2 = t;

        sort(temp1.begin(),temp1.end());
        sort(tmp2.begin(),tmp2.end());

        for(int i = 0; i < s.size(); i++)
        {
            if(temp1[i]!= tmp2[i])
            {
                return false;
            }
        }
        return true;
    }
};
