def func():
    for _ in range(int(input())):
        n = int(input())
        ar = list(sorted(list(map(int, input().split()))))
        print(sum([ar[i] - ar[i - 1] for i in range(1, n)]))

