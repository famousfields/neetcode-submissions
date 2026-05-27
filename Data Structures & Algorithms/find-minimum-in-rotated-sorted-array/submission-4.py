class Solution:
    def findMin(self, nums: List[int]) -> int:
      """
        [3,4,5,6,1,2]
                 l   
               r
        [4,5,0,1,2,3]
        l  r       

        [4,5,6,7]
        l       r
      """

      l,r = 0, len(nums)-1
      res = nums[0]

      while l <= r:
        if nums[l] < nums[r]:
            res = min(nums[l], res)
            break

        m = (l+r)//2
        res = min(nums[m], res)

        if nums[m] >= nums[l]:
            l = m+1
        else:
            r = m -1

      return res

        
            
        



                