# -- coding: utf-8 --

def f():
  l = 0
  n = int(input())
  S = 0
  while n != 0:
    l += 1
    S += n
    n = int(input())
  
  S = S/l
  
  print('')
  return(S)

print(f())