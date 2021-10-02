# -- coding: utf-8 --
def v(y):
    if (y % 4 == 0 and not y % 100 == 0) or y % 400 == 0:
        p = 'Да'
    else:
        p = 'Нет'
    return p

print(v(int(input())))