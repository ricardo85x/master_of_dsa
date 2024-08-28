def is_subsequence(word: str, sub: str) -> bool:
    i, j = 0, 0

    while i < len(sub) and j < len(word):
        if sub[i] == word[j]:
            i += 1
        j += 1

    return i == len(sub) 

if is_subsequence("abcde", "ace"):
    print("is sub")
else:
    print("it is not")