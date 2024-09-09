# Binary Search - Search a 2D Matrix

# Write an efficient algorithm that 
# searches for a value target 
# in an m x n integer matrix matrix. 
# Integers in each row are sorted from left to right. 
# The first integer of each row is 
# greater than the last 
# integer of the previous row.

def has_target(matrix: list[list[int]], target: int):
    m,n = len(matrix), len(matrix[0])
    
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        val = matrix[row][col]
        
        if val == target:
            return True
        if val > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return False

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

if( has_target(matrix, 3)):
    print("Found")
else:
    print("Not found")
    
