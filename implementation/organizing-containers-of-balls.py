def organizingContainers(container):
    
    ans = 'Possible'
    
    r_sum = [sum(i) for i in container]
    c_sum = [sum(row[i] for row in container) for i in range(len(container))]

    r_sum.sort()
    c_sum.sort()

    for i in range(len(container)):
        if r_sum[i] != c_sum[i]:
            ans = 'Impossible'

    return ans

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)

