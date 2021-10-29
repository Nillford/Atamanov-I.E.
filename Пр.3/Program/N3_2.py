# -- coding: utf-8 --

A = int(input())
B = int(input())
print()

def f(A,B):
	
	c = 1
	
	if A > B:
		c = -c
	
	for i in range(A, B+c, c):
		print(i)
	
	return ''

print(f(A,B))