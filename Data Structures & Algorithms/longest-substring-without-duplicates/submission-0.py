class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        count = 0
        maxCount = 0

        for i in range(len(s)):
            while s[i] in mySet:
                mySet.remove(s[count])
                count +=1
            mySet.add(s[i])
            maxCount = max(i-count+1,maxCount)
        return maxCount
        