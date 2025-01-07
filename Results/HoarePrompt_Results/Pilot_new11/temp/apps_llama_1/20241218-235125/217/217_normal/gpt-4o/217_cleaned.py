n = int(input())
a = list(map(int, input().split()))
B = sum((x for x in a if x > 0))
C = sum((x for x in a if x < 0))
result = B - C
print(result)