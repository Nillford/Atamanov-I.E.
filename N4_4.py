def q(a, b, l, N):
	if N > 0:
		s = 2*l + 2*b*(N-1) + 2*a*(N-1) + a
	else:
		s = 0
	return s

a = int(input())
b = int(input())
l = int(input())
N = int(input())

print(q(a, b, l, N))