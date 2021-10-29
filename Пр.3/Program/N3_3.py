# -- coding: utf-8 --

A = int(input())
B = int(input())
print()

def f(A,B):
	
	c = 0
	
	if A%2==0:
		c = 1
	
	for i in range(A-c, B-1, -2):
		print(i)
	
	return ''

print(f(A,B))