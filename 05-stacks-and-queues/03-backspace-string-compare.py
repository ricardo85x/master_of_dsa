# Backspace String Compare

# Given two strings s and t, 
# return true if they are equal when 
# both are typed into empty text editors.
# '#' means a backspace character.
#
# For example, given s = "ab#c" and t = "ad#c", 
# return true. 
# Because of the backspace, \
# the strings are both equal to "ac".

def compare_backspace(s: str, t: str) -> bool:
    stack_s : list[str] = []
    stack_t : list[str] = []

    def check(s: str) -> str:
        stack : list[str] = []
        for c in s:
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()

        return "".join(stack)

    return check(s) == check(t)
    

if compare_backspace("ab#c", "af#c"):
    print("Equal")
else:
    print("Not Equal")
