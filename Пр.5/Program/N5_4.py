# -- coding: utf-8 --

def f():
  x = int(input())
  y = int(input())
  print('')
  n = 1
  while x < y:
    x += x * 0.1
    n += 1
  
  return(n)

print(f())