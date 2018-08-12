def queensAttack(n, k, r_q, c_q, obstacles):

	board = [[1 for i in range(n)] for j in range(n)]

	ans = 0

	for r, c in obstacles:
		board[n - r][c - 1] = -1

	board[n - r_q][c_q - 1] = 0
	
	# for _ in range(n):
	# 	print(board[_])

	#right
	for i in range(n - c_q):
		if board[n - r_q][c_q + i] == 1:
			ans += 1
		else: 
			break

	# left 
	for i in range(1, c_q):
		if board[n - r_q][c_q - i - 1] == 1:
			ans += 1
		else: 
			break

	#top
	for i in range(n - r_q):
		if board[n - r_q - i - 1][c_q - 1] == 1:
			ans += 1
		else: 
			break
	
	#bottom
	for i in range(1, r_q):
		if board[n - r_q + i][c_q - 1] == 1:
			ans += 1
		else: 
			break

	# diagonal top right
	i = n - r_q - 1 
	j = c_q
	while (
		i >= 0
		and j < n
	):
		if board[i][j] == 1:
			ans += 1
		
		else:
			break

		i -= 1
		j += 1	
	
	# diagonal top left
	i = n - r_q - 1 
	j = c_q - 2
	while (
		i >= 0
		and j >= 0
	):
		if board[i][j] == 1:
			ans += 1
		
		else:
			break

		i -= 1
		j -= 1	
	
	# diagonal bottom left
	i = n - r_q + 1 
	j = c_q - 2
	while (
		i < n
		and j >= 0
	):
		if board[i][j] == 1:
			ans += 1
		
		else:
			break

		i += 1
		j -= 1	
	
	# diagonal bottom right
	i = n - r_q + 1 
	j = c_q
	while (
		i < n
		and j < n
	):
		if board[i][j] == 1:
			ans += 1
		
		else:
			break

		i += 1
		j += 1	

	# 
	return ans



if __name__ == '__main__':

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	r_qC_q = input().split()

	r_q = int(r_qC_q[0])

	c_q = int(r_qC_q[1])

	obstacles = []

	for _ in range(k):
		obstacles.append(list(map(int, input().rstrip().split())))

	result = queensAttack(n, k, r_q, c_q, obstacles)

	print(result)
