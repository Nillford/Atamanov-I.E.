# -- coding: utf-8 --

n = int(input())
print()

def f(n):
	S = 1
	for i in range(n):
		S *= i+1
	
	return S


print(f(n))