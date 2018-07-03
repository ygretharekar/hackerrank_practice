
def plusMinus(arr):
	a = len(arr)
	p = [ i for i in arr if i > 0]
	n = [ i for i in arr if i < 0]
	z = [ i for i in arr if i == 0]
	print('{0:.6f}'.format(len(p)/a))
	print('{0:.6f}'.format(len(n)/a))
	print('{0:.6f}'.format(len(z)/a))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
