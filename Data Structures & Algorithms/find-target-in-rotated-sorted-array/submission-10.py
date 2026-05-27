class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        [3,4,5,6,1,2]
        l           r
        [1,3]
        l  r


        [5,1,3]
        l    r

        [5,1,2,3,4]
        l        r
        """
        l,r = 0, len(nums) - 1

        while l<=r:
            m = (l+r) //2

            if nums[m] == target:
                return m
            #left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m + 1  

        return -1

        