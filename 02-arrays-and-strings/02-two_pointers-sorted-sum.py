def check_for_target(arr: list[int], target: int):
    
    left = 0
    right = len(arr) - 1

    while left < right:
        the_sum =  arr[left] + arr[right]
        if the_sum == target:
            print("Found ",  arr[left],  arr[right])
            return True
        if the_sum > target:
            right -=1
        else:
            left += 1
    
    print("Not found")
    return False

l1 = [1,2,3,4,7,9,14,15]

target = 13

check_for_target(l1, target)