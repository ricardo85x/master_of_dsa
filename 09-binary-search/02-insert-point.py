# Binart Search - Insert point

def binary_search(items: list[int], target: int) -> int:
    left = 0
    right = len(items) - 1
    
    while left < right:
        mid = (left + right) // 2
        if items[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

print(binary_search([1,4,8,8,13,13,20], 13))
