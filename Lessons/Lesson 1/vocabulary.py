words = {}
while True:
    s = input()
    if s in words:
        print("Word", s, "is traslated", words[s])
    else:
        print("Please, write translate", s)
        words[s] = input()