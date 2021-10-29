# -- coding: utf-8 --

S = input()
print()

def f(S):

	if not S.find('f') == -1:
		print(S.find('f'))

	if not S.rfind('f') == S.find('f'):
		print(S.rfind('f'))
	
	return ''


print(f(S))