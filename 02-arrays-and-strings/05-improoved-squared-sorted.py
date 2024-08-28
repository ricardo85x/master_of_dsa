def sortedSquares(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        square = 0
        if(abs(nums[left]) < abs(nums[right])):
            square = nums[right] ** 2
            right -= 1
        else:
            square = nums[left] ** 2
            left += 1
            
        result[i] = square
    
    return result

print(sortedSquares([-4,-1,0,3,10]))