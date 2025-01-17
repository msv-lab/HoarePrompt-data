t = int(input())

for _ in range(t):
    n,k = map(int,input().split(" "))
    output = []
    for j in range(n):
        for i in range(k):
            output.append(chr(ord('a') + i))

    print("".join(output))