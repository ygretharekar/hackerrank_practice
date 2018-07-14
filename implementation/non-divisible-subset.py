def nonDivisibleSubset(k, S):
    remainder = [0 for i in range(k)]

    for i in S:
        remainder[i%k] += 1

    # print(remainder)

    ans = 0

    ans += 1 if remainder[0] >= 1 else 0

    if k%2 == 0:
        ans += 1 if remainder[k//2] >= 1 else 0

    mid = k//2 if k%2 == 1 else k//2 - 1 

    """ if mid == 1:
        ans += max(remainder[1], remainder[k - 1]) """

    # else:
    for i in range(1, mid+1):
        ans += max(remainder[i], remainder[k - i])

    return ans

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    """ for i in range(1, 1):
        print('aaaaaa') """

    print(result)
