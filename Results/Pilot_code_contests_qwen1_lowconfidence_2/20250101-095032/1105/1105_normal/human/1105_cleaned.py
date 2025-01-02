rints = lambda : [int(x) for x in stdin.readline().split()]
(n, a) = (int(input()), rints())
neg = len(list(filter(lambda x: x < 0, a)))
pos = n - neg
if neg:
    print(sum((abs(x) for x in a)))
else:
    (ans, s) = (0, sum(a))
    for i in range(n):
        if i and a[i] < a[i - 1]:
            ans = max(ans, s - a[i - 1])
        elif i < n - 1 and a[i] < a[i + 1]:
            ans = max(ans, s - a[i + 1])
    print(ans)