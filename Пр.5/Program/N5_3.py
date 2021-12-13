# -- coding: utf-8 --

def f():
  N = int(input())
  i = 0
  a = 1
  while a*2 <= N:
    a *= 2
    i += 1
  
  return(i, a)

print(f())