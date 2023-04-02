# NWD - największy wspólny dzielnik (największa liczba, która dzieli obydwie podane)
# NWW - najmniejsza wspólna wielokrotność (namniejsza liczba, która dzieli sie przez obydwie podane)

def euklides_iter(a,b):
    pom = 0
    while (b != 0):
        pom = b
        b = a % b
        a = pom

    return(a)

def euklides_reku(a,b):
    if b != 0:
        return euklides_reku(b, a%b)

    return(a)

def nww(a,b):
    return int (a/euklides_reku(a,b)*b)

a,b= 24, 36

print(euklides_iter(a,b))
print(euklides_reku(a,b))
print(nww(a,b))