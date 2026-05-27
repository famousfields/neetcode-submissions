class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []

        for i, a in enumerate(nums):# allows you to keep both value and index

            if i > 0 and a == nums[i-1]:
                continue
                
            l,r = i+1, len(nums)-1

            while l < r:
                res = a + nums[l] + nums[r]
                if res > 0:
                    r = r-1
                elif res < 0:
                    l = l+1
                else:
                    lst.append([a,nums[l],nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return lst

