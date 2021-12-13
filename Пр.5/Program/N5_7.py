# -- coding: utf-8 --

def f():
  m = int(input())
  n = int(input())
  S = 0
  while n != 0:
    if n > m:
      S += 1
    m = n
    n = int(input())
  
  print('')
  return(S)

print(f())