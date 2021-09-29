def q(n, m, k):
	s = "Нет"
	for i in range(n):
		if n*i == k:
			s = "Да"
	for i in range(m):
		if m*i == k:
			s = "Да"
	return s

n = int(input())
m = int(input())
k = int(input())

print(q(n, m, k))