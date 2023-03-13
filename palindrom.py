"""
Palindrom - wyraz czytany od tyłu brzmi tak samo jak czytany normalnie, np. kajak
"""

def czy_palindrom(w: str):
    i,j = 0, len(w)-1

    while(i!=j):
        if(w[i] != w[j]):
            return False
        i+=1
        j-=1

    return True


print(czy_palindrom('kajak'))
print(czy_palindrom('niepalindrom'))
print(czy_palindrom('kobyłamamałybok'))
