n = int(input())
a = list(map(int, input().split()))

odd_count = 0
for x in a:
    if x % 2 == 1:
        odd_count += 1

if odd_count < 2:
    print("No")
else:
    print("Yes")
