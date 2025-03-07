for _ in range(int(input())):
    (n, m, k) = map(int, input().split())
    a = list(map(int, input().split()))
    todo = set(map(int, input().split()))
    done = set()
    extra = set()
    for j in range(m):
        if a[j] in todo:
            todo.remove(a[j])
            done.add(a[j])
        else:
            extra.add(a[j])
    ans = 1 if len(done) >= k else 0
    for r in range(m, n):
        old = a[r - m]
        if old in extra:
            extra.remove(old)
        elif old in done:
            done.remove(old)
            todo.add(old)
        if a[r] in todo:
            todo.remove(a[r])
            done.add(a[r])
        else:
            extra.add(a[r])
        if len(done) >= k:
            ans += 1
    print(ans)