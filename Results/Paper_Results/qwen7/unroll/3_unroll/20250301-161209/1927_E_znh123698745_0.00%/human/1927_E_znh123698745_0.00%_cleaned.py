for _ in range(int(input())):
    (n, k) = map(int, input().split())
    array = list(range(1, n + 1))
    answer = [1]
    a = [1, -1]
    for i in range(1, n):
        if (-1) ** i == -1:
            answer.append(array[a[-1]])
            a[-1] -= 1
        else:
            answer.append(array[a[0]])
            a[0] += 1
    print(*answer)