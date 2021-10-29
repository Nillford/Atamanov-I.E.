# -- coding: utf-8 --

S = input()
print()

def f(S):
	S = S[S.find(' ')+1:] + ' ' + S[:S.find(' ')]
	
	return S


print(f(S))