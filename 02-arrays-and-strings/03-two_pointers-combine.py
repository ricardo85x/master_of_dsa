# Given two sorted integer arrays arr1 and arr2, 
# return a new array that combines both of them and is also sorted.

def combine(arr1: list[int], arr2: list[int]) -> list[int]:
    ans = []
    i,j = 0, 0

    while i < len(arr1) and j < len(arr2):
      if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
      else:
        ans.append(arr2[j])
        j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = combine(arr1, arr2)
print(result) 