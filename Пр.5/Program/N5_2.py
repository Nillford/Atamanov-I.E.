# -- coding: utf-8 --

def f():
  N = 0
  while N < 2:
    print ('Число введите не меньше 2')
    N = int(input())
  print('')
  i = 2
  while N%i != 0:
    i += 1
  
  return(i)

print(f())