n = int(input())
juices = []
for _ in range(n):
    price, vitamins = input().split()
    juices.append((int(price), vitamins))

min_price = float('inf')
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            all_vitamins = set(juices[i][1] + juices[j][1] + juices[k][1])
            if len(all_vitamins) == 3:
                total_price = juices[i][0] + juices[j][0] + juices[k][0]
                min_price = min(min_price, total_price)

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)