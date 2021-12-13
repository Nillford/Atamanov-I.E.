# -- coding: utf-8 --

def f():
  m = int(input())
  n = int(input())
  S = 1
  M = 1
  while n != 0:
    if n == m:
      S += 1
    else:
      S = 1
    if S > M:
      M = S
    m = n
    n = int(input())
  
  print('')
  return(M)

print(f())