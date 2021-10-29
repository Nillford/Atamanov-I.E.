# -- coding: utf-8 --

N = int(input())
K = int(input())
print()

def f(N,K):
	S = 0
	a = 0
	b = 1
	c = 1
	
	for i in range(N+K-1):
		if (i+1) >= K:
			S += c
		
		c = a + b
		a = b
		b = c
	
	return S


print(f(N,K))