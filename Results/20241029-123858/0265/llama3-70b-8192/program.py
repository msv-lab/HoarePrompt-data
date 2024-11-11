n, m = map(int, input().split())
friends = []
for _ in range(n):
    f_i = list(map(int, input().split()))
    friends.append(set(f_i[1:]))

pizzas = []
for _ in range(m):
    c_j, r_j = map(int, input().split())
    a_jt = set(map(int, input().split()[1:]))
    pizzas.append((c_j, a_jt))

ans = (-1, -1)
max_pleased = 0
min_price = float('inf')

for i in range(m):
    for j in range(i+1, m):
        pleased = 0
        for f in friends:
            if f.issubset(pizzas[i][1]) or f.issubset(pizzas[j][1]):
                pleased += 1
        if pleased > max_pleased:
            max_pleased = pleased
            min_price = pizzas[i][0] + pizzas[j][0]
            ans = (i+1, j+1)
        elif pleased == max_pleased:
            if pizzas[i][0] + pizzas[j][0] < min_price:
                min_price = pizzas[i][0] + pizzas[j][0]
                ans = (i+1, j+1)

print(*ans)
