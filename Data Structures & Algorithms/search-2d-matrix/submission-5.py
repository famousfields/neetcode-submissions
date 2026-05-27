class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        [1,  2, 4, 8]
        [10,11,12,13]
        [14,20,30,40]
        """

        ROW, COL = len(matrix), len(matrix[0])
        top,bot = 0, ROW-1
        l,r = 0, COL-1

        while top<=bot:
            mRow = (top + bot) // 2

            if matrix[mRow][l] <= target and matrix[mRow][r] >= target:
                while l <= r:
                    m = (l+r)//2

                    if matrix[mRow][m] == target:
                        return True
                    elif matrix[mRow][m] > target:
                        r = m - 1
                    else:
                        l = m + 1

            elif target < matrix[mRow][l]:
                bot = mRow - 1
            else:
                top = mRow+1

        return False
            


