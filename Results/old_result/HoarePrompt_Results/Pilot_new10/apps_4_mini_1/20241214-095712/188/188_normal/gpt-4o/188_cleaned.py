n = int(input())
cards = [int(input()) for _ in range(n)]
count = Counter(cards)
unique_numbers = sorted(count.keys(), key=lambda x: count[x])
if len(unique_numbers) < 2:
    print('NO')
elif count[unique_numbers[-1]] == n // 2 and count[unique_numbers[-2]] == n // 2:
    print('YES')
    print(unique_numbers[-1], unique_numbers[-2])
else:
    print('NO')