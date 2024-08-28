def sentence_is_pangram(s: str):
    unique = set(s)

    return len(unique) == 26

if sentence_is_pangram("thequickbrownfoxjumpsoverthelazydog"):
    print("is pangram")
else:
    print("it is not pangram")