MIN_VALUE = 10**8

def is_magic_square(s):
	""" if (s[0][0] + s[0][1] + s[0][2] == 15 and
		s[1][0] + s[1][1] + s[1][2] == 15 and
		s[2][0] + s[2][1] + s[2][2] == 15 and
		s[0][0] + s[1][0] + s[2][0] == 15 and
		s[0][1] + s[1][1] + s[2][1] == 15 and
		s[0][2] + s[1][2] + s[2][2] == 15 and
		s[0][0] + s[1][1] + s[2][2] == 15 and
		s[0][2] + s[1][1] + s[2][0] == 15):
		print(s) """

	return(s[0][0] + s[0][1] + s[0][2] == 15 and
		   s[1][0] + s[1][1] + s[1][2] == 15 and
		   s[2][0] + s[2][1] + s[2][2] == 15 and
		   s[0][0] + s[1][0] + s[2][0] == 15 and
		   s[0][1] + s[1][1] + s[2][1] == 15 and
		   s[0][2] + s[1][2] + s[2][2] == 15 and
		   s[0][0] + s[1][1] + s[2][2] == 15 and
		   s[0][2] + s[1][1] + s[2][0] == 15)

def search_magic(m, n, r, c, s):
	if r == 3:
		if is_magic_square(m):
			cost = 0
			global MIN_VALUE
			for rows, rowm in zip(s, m):
				for eles, elem in zip(rows, rowm):
					cost += abs(eles - elem)

			MIN_VALUE = min(MIN_VALUE, cost)
			# print(MIN_VALUE)	

		return

	if c == 3:
		search_magic(m, n, r + 1, 0, s)
		return

	index = r*3 + c

	for i in range(index, len(n)):
		n[index], n[i] = n[i], n[index]
		m[r][c] = n[index]
		search_magic(m, n, r, c + 1, s)
		n[index], n[i] = n[i], n[index]
		# print(n)

def make_magic_square(s):
	n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	m = [[0, 0, 0] for _ in range(3) ]
	# m = [[0]*3]*3

	# print(m)

	search_magic(m, n, 0, 0, s)

if __name__ == '__main__':
	s = [ list(map(int, input().rstrip().split())) for i in range(3) ]
	make_magic_square(s)

	print(MIN_VALUE)
	# search_magic(s, 0, 4, 0, s)
