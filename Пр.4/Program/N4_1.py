# -- coding: utf-8 --

S = input()
print()

def f(S):
	print(1,S[2])
	print(2,S[-2])
	print(3,S[:5])
	print(4,S[:-2])
	print(5,S[::2])
	print(6,S[1::2])
	print(7,S[::-1])
	print(8,S[::-2])
	print(9,len(S))
	
	return ''


print(f(S))