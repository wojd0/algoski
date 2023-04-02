def cyfry_bez_tablic(n):
    while n > 0:
        print(n%10)
        n //= 10;

cyfry_bez_tablic(1234)