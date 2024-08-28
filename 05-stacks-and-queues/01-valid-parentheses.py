# Valid Parentheses

# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid. 
# The string is valid if all open brackets 
# are closed by 
# the same type of closing bracket 
# in the correct order, 
# and each closing bracket 
# closes exactly one open bracket.

# For example, 
# s = "({})" and s = "(){}[]" are valid, 
# but s = "(]" and s = "({)}" are not valid.

def is_valid_parentheses(s: str) -> bool:
    matching = { "(": ")", "[" : "]", "{": "}"}
    stack = []
    for c in s:
        if c in matching:
            stack.append(c)
        else:
            if not stack:
                return False
            prev_opening = stack.pop()
            if matching[prev_opening] != c:
                return False

    return not stack

            
if is_valid_parentheses("(){}[]"):
    print("Valid matching")
else:
    print("Invalid matching")