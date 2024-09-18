# Count 1 from binary string

# You are given a 
#   binary string s (a string containing only "0" and "1"). 

# You may choose up to one "0" and flip it to a "1". 

# What is the length of the longest substring 
# achievable that contains only "1"?

# Example, 
# given 
#   s = "1101100111", 
# the answer is 5. 
#   If you perform the flip at index 2, 
#   the string becomes 1111100111.

# Because the string can only contain 
#   "1" and "0"
# and you can flip ONE '0' to '1'
# another way to look at this problem is 
#   "what is the longest substring 
#   that contains at most one "0"?"

def find_length(s: str):
    left = curr = ans = 0
    
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
               curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

print(find_length("1101100111"))