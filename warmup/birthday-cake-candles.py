from functools import reduce

def birthdayCakeCandles(ar):
    highest = reduce(lambda x, y: x if x > y else y, ar)

    count = reduce(lambda x, y: x + 1 if y == highest else x, ar, 0)

    return count

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
	
    print(result)