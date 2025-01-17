def color_uniform(n, m, k):
    if m == k or k > n:
        return "NO"
    elif m > k:
        return "YES"
    else:
        return "NO"
    


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    print(color_uniform(n, m, k))