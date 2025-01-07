A, B, C, N = map(int, input().split())
total_visited = A + B - C
if total_visited > N or C > A or C > B:
    print(-1)
else:
    print(N - total_visited)
