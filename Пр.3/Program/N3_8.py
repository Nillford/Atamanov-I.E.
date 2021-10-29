# -- coding: utf-8 --

n = int(input())
print()

def f(n):
	s = str()
	for i in range(1, n+1):
		for j in range(i):
			s = s + str(j+1)
		print(s)
		s = ''
	
	return ''


print(f(n))