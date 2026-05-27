class Solution {
public:
    bool isPalindrome(string s) 
    {   
        stack <char> stack;
        queue<char> queue;

        for(char c: s)
        {
            if(isalnum(c))
            {
                char lowerC = std::tolower(c);

                stack.push(lowerC);
                queue.push(lowerC);
            }
        }

        while (!stack.empty() && !queue.empty())
        {
            char temp = stack.top();
            char temp2 = queue.front();
            stack.pop();
            queue.pop();
            if(temp != temp2)
            {
                return false;
            }
        }
        
        return stack.empty() && queue.empty();
    }
};
