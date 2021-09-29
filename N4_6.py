def fun(a, b, c, d):
    if (a + b) % 2 == 0:
        ab = 1
    else:
        ab = 0
    
    if (c + d) % 2 == 0:
        cd = 1
    else:
        cd = 0
    
    if ab == cd:
        p = 'Да'
    else:
        p = 'Нет'
    return p

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(fun(a, b, c, d))

