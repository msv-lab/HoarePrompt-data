n = int(input())
ratings_before = []
ratings_after = []
for _ in range(n):
    a, b = map(int, input().split())
    ratings_before.append(a)
    ratings_after.append(b)

rated = False
unrated = True
maybe = True

for i in range(n):
    for j in range(i+1, n):
        if ratings_before[i] < ratings_before[j] and ratings_after[i] > ratings_after[j]:
            unrated = False
            break
    if not unrated:
        break

for i in range(n):
    if ratings_before[i] != ratings_after[i]:
        rated = True
        break

if rated:
    print("rated")
elif unrated:
    print("unrated")
else:
    print("maybe")
