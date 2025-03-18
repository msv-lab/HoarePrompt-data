def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        x += min(a[i], b[i])
    print(pergunta)
numCasos = int(input())
for i in range(numCasos):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pergunta = float('inf')
    func_1(pergunta, a, b, n, m)