# -- coding: utf-8 --

N = int(input())
print()

def f(N):
	S = 0
	a = 0
	b = 1
	c = 1
	
	for i in range(N):
		S += c
		
		c = a + b
		a = b
		b = c
	
	return S


print(f(N))