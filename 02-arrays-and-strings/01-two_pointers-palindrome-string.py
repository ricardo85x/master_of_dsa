def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while(left < right):

        if(s[left] != s[right]): 
            return False
        
        left += 1
        right -= 1

    return True

if is_palindrome(input()):
    print("It is Palindrome")
else:
    print("It is not palindrome")
