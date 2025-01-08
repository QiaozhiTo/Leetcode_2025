class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l2, r2 = 0, len(matrix[m])-1
                while l2 <= r2:
                    m2 = (l2+r2)//2
                    if matrix[m][m2] < target:
                        l2 = m2 + 1
                    elif matrix[m][m2] > target:
                        r2 = m2 - 1
                    else:
                        return True
                return False
        return False

