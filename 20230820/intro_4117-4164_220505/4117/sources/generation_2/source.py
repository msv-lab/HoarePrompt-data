N = int(input())
sticks = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a, b, c = sticks[i], sticks[j], sticks[k]
            if a != b and b != c and a != c and a+b > c and b+c > a and a+c > b:
                count += 1

print(count)