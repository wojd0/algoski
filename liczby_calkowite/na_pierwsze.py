def na_pierwsze(n):
    k = 2
    while n > 1:
        while n % k == 0:
            n = n // k
            print(k)
        k += 1

na_pierwsze(47)