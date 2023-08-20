N, K, Q = map(int, input().split())
answers = [0] * N

for _ in range(Q):
    A = int(input())
    answers[A-1] += 1

for i in range(N):
    if answers[i] >= Q:
        print("Yes")
    else:
        print("No")