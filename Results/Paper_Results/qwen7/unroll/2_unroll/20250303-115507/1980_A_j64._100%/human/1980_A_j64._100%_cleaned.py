def func_1(n, m, a):
    count = [0] * 7
    for char in a:
        count[ord(char) - ord('A')] += 1
    needed_problems = 0
    for i in range(7):
        if count[i] < m:
            needed_problems += m - count[i]
    return needed_problems
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    a = input()
    print(func_1(n, m, a))