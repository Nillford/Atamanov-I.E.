# -- coding: utf-8 --
def min(a, b, c):
    if a < b and a < c:
        m = a
    elif b < c:
        m = b
    else:
        m = c
    return m

a = int(input())
b = int(input())
c = int(input())

print(min(a, b, c))