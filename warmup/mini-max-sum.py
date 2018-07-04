from functools import reduce

def miniMaxSum(arr):
	total = reduce(lambda x, y: x + y, arr)
	sums = [ total - i for i in arr ]
	print(min(sums), max(sums))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
