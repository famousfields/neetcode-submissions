class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = {}
        count = 0
        l = 0 
        maxF = 0

        for r in range(len(s)):
            res[s[r]] = 1 + res.get(s[r],0)
            maxF = max(maxF, res[s[r]])

            while( r-l+1) - maxF > k:
                res[s[l]] -= 1
                l+=1
            count = max(count, r-l+1)
        return count
        
        