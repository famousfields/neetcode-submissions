class Solution:
    def findMin(self, nums: List[int]) -> int:
      """
        [3,4,5,6,1,2]
                  l r

        [4,5,0,1,2,3]
             l     r

        [4,5,6,7]
        l       r
      """

      l,r = 0, len(nums)-1

      while l <= r:
        m = (l+r) // 2

        if nums[l] > nums[r]:
            l = m+1
        elif (l-1)>0 and nums[l-1] < nums[l]:
            l -= 1
        else:
            return nums[l]

        
            
        



                