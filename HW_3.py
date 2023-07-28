phrase = input("Enter phrase:")
phrase_len_unique = len(set(phrase))
if phrase_len_unique > 10:
    print(True)
else:
    print(False)



