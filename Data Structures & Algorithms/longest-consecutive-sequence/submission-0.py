class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        nums.sort()
        
        count, maxCount = 1,1

   
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1  # reset count for a new sequence
            maxCount = max(maxCount, count)

        return maxCount