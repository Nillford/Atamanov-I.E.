# -- coding: utf-8 --
def q(a, b, c):
    if a == b and b == c:
        p = 3
    elif a == b or b == c or a == c:
        p = 2
    else:
        p = 0
    return(p)

a = int(input())
b = int(input())
c = int(input())

print(q(a, b, c))