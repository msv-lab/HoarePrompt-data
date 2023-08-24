D, N = map(int, input().split())

if D == 0:
    print(N)
elif D == 1:
    print(N * 101)
elif D == 2:
    print(N * 10100)
else:
    print("Invalid value for D. D should be 0, 1, or 2.")