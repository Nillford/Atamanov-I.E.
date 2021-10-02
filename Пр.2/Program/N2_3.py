# -- coding: utf-8 --
def c(m):
    m = int(m)
    m = m % (60 * 24)
    
    h = m // 60
    m = m % 60
    if h < 10:
        h = str(h)
        h = '0' + h
    else:
        h = str(h)
    if m < 10:
        m = str(m)
        m = '0' + m
    else:
        m = str(m)
    return h + ':' + m

m = input()

print(c(m))