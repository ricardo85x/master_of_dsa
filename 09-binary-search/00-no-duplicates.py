# Binary search 
# with no duplicates input

def binary_search(items: list[int], target: int) -> int:
    left = 0
    right = len(items) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2 # // 2 is floor division
        if items[mid] == target:
            return mid
        if items[mid] > target:
            right = mid - 1
        else:
            left = mid + 1    
    
    return result

print(binary_search([1,4,8,12,13,20], 9))


        