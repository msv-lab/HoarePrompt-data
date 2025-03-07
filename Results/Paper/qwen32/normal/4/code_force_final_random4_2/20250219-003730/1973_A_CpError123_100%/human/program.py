t = int(input())  # Lecture du nombre de cas de test
for _ in range(t):
    a, b, c = map(int, input().split())  # Lecture des trois entiers
    if (a + b + c) % 2 != 0:
        print(-1)
        continue
    x = (a + b + c) // 2
    y = a + b
    print(min(x, y))