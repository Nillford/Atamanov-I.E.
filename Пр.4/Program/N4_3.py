# -- coding: utf-8 --

S = input()
print()

def f(S):
	S = S[len(S)//2+1:] + S[:len(S)//2+1]
	
	return S


print(f(S))