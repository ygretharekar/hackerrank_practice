def queensAttack(n, k, r_q, c_q, obstacles):

	ans = 0
	
	board = [[1 for i in range(n)] for j in range(n)]

	for r, c in obstacles:
		board[n - r][c - 1] = -1

	board[n - r_q][c_q - 1] = 0
	
	for _ in range(n):
		print(board[_])

	r_obs_c = -1
	r_obs_r = -1
	l_obs_c = -1
	l_obs_r = -1
	t_obs_c = -1
	t_obs_r = -1
	b_obs_c = -1
	b_obs_r = -1
	rt_obs_c = -1
	rt_obs_r = -1
	lt_obs_c = -1
	lt_obs_r = -1
	rb_obs_c = -1
	rb_obs_r = -1
	lb_obs_c = -1
	lb_obs_r = -1

	for r, c in obstacles:
		# board[n - r][c - 1] = -1

		if r == r_q:
			#right
			if ((c < r_obs_c or r_obs_r == -1)
				and c > c_q):
				r_obs_c = c
				r_obs_r = r
			
			#left
			if ((c > l_obs_c or l_obs_r == -1)
				and c < c_q):
				l_obs_c = c
				l_obs_r = r
		
		if c == c_q:
			#top
			if ((r < t_obs_r or t_obs_c == -1)
				and r > r_q):
				t_obs_c = c
				t_obs_r = r
			
			#bottom
			if ((r > b_obs_r or b_obs_c == -1)
				and r < r_q):
				b_obs_c = c
				b_obs_r = r

		#top right
		if ((c - c_q == r - r_q and c > c_q and r > r_q)
			and ((c < rt_obs_c and r < rt_obs_r) or rt_obs_c == -1 )):

			rt_obs_c = c
			rt_obs_r = r
		
		#top left
		if ((c_q - c == r - r_q and c < c_q and r > r_q)
			and ((c > lt_obs_c and r < lt_obs_r) or lt_obs_c == -1 )):

			lt_obs_c = c
			lt_obs_r = r
		
		#bottom right
		if ((c - c_q == r_q - r and c > c_q and r < r_q)
			and ((c < rb_obs_c and r > rb_obs_r) or rb_obs_c == -1 )):

			rb_obs_c = c
			rb_obs_r = r
		
		#bottom left
		if ((c_q - c == r_q - r and c < c_q and r < r_q)
			and ((c > lb_obs_c and r > lb_obs_r) or lb_obs_c == -1 )):

			lb_obs_c = c
			lb_obs_r = r

	#right
	if r_obs_r > 0:
		ans += r_obs_c - c_q - 1
		# print(ans)

	else:
		ans += n - c_q
		# print(ans)


	#left
	if l_obs_r > 0:
		ans += c_q - l_obs_c - 1
		# print(ans)


	else:
		ans += c_q - 1
		# print(ans)


	#top
	if t_obs_c > 0:
		ans += t_obs_r - r_q - 1
		# print(ans)


	else:
		ans += n - r_q
		# print(ans)


	#bottom
	if b_obs_c > 0:
		ans += r_q - b_obs_r - 1
		# print(ans)


	else:
		ans +=r_q - 1
		# print(ans)


	#top right
	if rt_obs_c > 0:
		# print(rt_obs_r, ' rt_obs_r ',rt_obs_c)
		ans += rt_obs_r - r_q - 1

	else:
		ans += min(n - r_q, n - c_q)
		# print(rt_obs_r, ' rt_obs_r ',min(n - r_q, n - c_q - 1 ))
	
	#top left
	if lt_obs_c > 0:
		# print(lt_obs_r, ' lt_obs_r ',lt_obs_c)
		ans += lt_obs_r - r_q - 1

	else:
		ans += min(n - r_q, c_q )
		# print(lt_obs_r, ' lt_obs_r ', min(n - r_q, c_q - 1 ))
	
	#bottom right
	if rb_obs_c > 0:
		# print(rb_obs_r, ' rb_obs_r ',rb_obs_c)
		ans += r_q - rb_obs_r - 1

	else:
		ans += min(r_q - 1, n - c_q)
		# print(rb_obs_r, ' rb_obs_r ', min(r_q - 1, n - c_q))
	
	#bottom left
	if lb_obs_c > 0:
		# print(lb_obs_r, ' lb_obs_r ', lb_obs_c)
		ans += r_q - lb_obs_r - 1

	else:
		ans += min(r_q - 1, c_q - 1)
		# print(lb_obs_r, ' lb_obs_r ', min(r_q - 1, c_q - 1))

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
