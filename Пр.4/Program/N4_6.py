# -- coding: utf-8 --

S = input()
print()

def f(S):

	if S.count('f') > 1:
		S = S.find('f',S.find('f')+1)
	else:
		if S.count('f') == 1:
			S = -1
		else:
			S = -2
	
	return S


print(f(S))