# -- coding: utf-8 --

S = input()
print()

def f(S):

	S = S[:S.find('h')] + S[S.rfind('h')+1:]
	
	return S


print(f(S))