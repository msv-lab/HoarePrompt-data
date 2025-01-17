n, k = map(int, input().split())
p = list(map(int, input().split()))
stack = []
for i in range(k, n):
    while stack and stack[-1] < n - i:
        stack.pop()
    if not stack or stack[-1] > p[-1]:
        p.append(n - i)
    else:
        break
    stack.append(n - i)
if len(p) != n:
    print(-1)
else:
    print(' '.join(map(str, p)))
