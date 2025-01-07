n = int(input())
ratings = []
is_rated = False
is_unrated = False
for _ in range(n):
    (a, b) = map(int, input().split())
    ratings.append((a, b))
    if a != b:
        is_rated = True
if not is_rated:
    for i in range(1, n):
        if ratings[i - 1][0] < ratings[i][0]:
            is_unrated = True
            break
if is_rated:
    print('rated')
elif is_unrated:
    print('unrated')
else:
    print('maybe')