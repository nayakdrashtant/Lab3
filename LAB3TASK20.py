import random
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)

    rand = []
    length = len(res)
    for r in res:
        num = random.randint(0,5)
        rand.insert(num,r)
    print("Main list:",res)
    return rand

x = input("Enter words:")
print("Random list:",sort_by_length(x))
