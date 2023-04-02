# anagram - slowo utworzone z przestawionych liter innego slowa (adam - dama)

def czy_anagram(a, b):
    if len(a) != len(b): return False

    licz = [0 for x in range(127)]

    for i in a:
        licz[ord(i)] += 1

    for i in b:
        licz[ord(i)] -= 1

    for i in licz:
        if i != 0: return False
    return True

print(czy_anagram('adam', 'dama'))