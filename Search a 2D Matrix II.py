def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(matrix == None or len(matrix) < 1 or len(matrix[0]) <1):            
            return False
        col=len(matrix[0])-1
        row=0
        while col >=0 and row <= len(matrix)-1:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col=col-1
            elif target > matrix[row][col]:
                row=row+1
        return False 
