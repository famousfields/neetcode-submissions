class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1 
        i = 0

        while i < n-1:
            tmp = one
            one = one + two
            two  = tmp
            i +=1
        return one
            