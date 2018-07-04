def show_mil_time(s):
    ans = s
    if s[-2:] == 'AM' and s[:2] == '12':
        ans = '00' + s[2:len(s) - 2]

    elif s[-2:] == 'AM' or (s[-2:] == 'PM' and s[:2] == '12'):
        ans = s[:len(s) - 2]

    else:
        ans = str(int(s[:2])+12) + s[2:len(s) - 2]

    return ans

if __name__ == '__main__':
	s = input()
	ans = show_mil_time(s)
	print(ans)
