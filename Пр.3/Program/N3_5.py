# -- coding: utf-8 --

n = int(input())
print()

def f(n):
	S = 0
	for i in range(n):
		S += (i+1)**3
	
	return S


print(f(n))