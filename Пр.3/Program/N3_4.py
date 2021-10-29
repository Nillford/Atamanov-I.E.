# -- coding: utf-8 --

N = int(input())
print()

def f(N):
	S = 0
	for i in range(N):
		S += int(input())
	
	print()
	return S


print(f(N))