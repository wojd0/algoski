def na_pierwsze(l):
    k = 2
    while l > 1:
        while l % k == 0:
            l = l//k
            print(k)
        k += 1

na_pierwsze(231235)