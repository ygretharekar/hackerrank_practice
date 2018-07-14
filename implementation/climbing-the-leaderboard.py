def get_ranks(scores):
    rank = 0
    ranks = []
    prev = 10**9 + 1
    for i in scores:
        if i < prev:
            rank += 1
        ranks += [rank]
        prev = i

    return ranks

def alice_rank(scores, ranks,score):
    l = 0
    u = len(scores) - 1
    rank = 1

    while u >= l:
        middle = (l + u)//2
        # print(middle, end=' ')
        if score == scores[middle]:
            rank = ranks[middle]
            break
            
        elif score < scores[middle]:
            rank = ranks[middle] + 1
            l = middle + 1
        
        else:
            u = middle - 1

    # print('')

    return rank

def climbingLeaderboard(scores, alice):
    ranks = get_ranks(scores)
    ans = [ alice_rank(scores, ranks, i) for i in alice ]
    return ans

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    # result = get_ranks(scores)

    # print(result)

    for i in result:
        print(i)
