n, k = map(int, input().split())
seen = set()
for i in range(1, k+1):
    remainder = n % i
    if remainder in seen:
        print("No")
        exit()
    seen.add(remainder)
print("Yes")
