def max_score(N, K, R, S, P, T):
    score = 0
    for i in range(N):
        if i < K or T[i] != T[i-K]:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
    return score

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

print(max_score(N, K, R, S, P, T))