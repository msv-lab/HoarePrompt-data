def max_score(N, K, R, S, P, T):
    score = 0
    played = [""] * N   # To keep track of the hands played in previous rounds
    for i in range(N):
        if i < K or T[i] != played[i-K]:
            if T[i] == "r":
                score += R
                played[i] = "r"
            elif T[i] == "s":
                score += S
                played[i] = "s"
            else:
                score += P
                played[i] = "p"
    return score

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

print(max_score(N, K, R, S, P, T))