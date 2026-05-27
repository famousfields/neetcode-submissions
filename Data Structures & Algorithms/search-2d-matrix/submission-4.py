class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l ,r = 0, len(matrix[0])-1

        while l < len(matrix):
            
            if target > matrix[l][r]:
                l += 1
                r = len(matrix[0])-1
            elif target < matrix[l][r]:
                r -= 1
                if r < 0: return False
            else:
                return True
        return False
        