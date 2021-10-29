# -- coding: utf-8 --

n = int(input())
print()

def f(n):
	P = 1
	S = 0
	for i in range(n):
		P *= i+1
		S += P
	
	return S


print(f(n))