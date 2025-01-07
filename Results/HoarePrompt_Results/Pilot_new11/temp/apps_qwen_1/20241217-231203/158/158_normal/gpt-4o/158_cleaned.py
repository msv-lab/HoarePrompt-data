a = int(input())
b = int(input())
c = int(input())
max_lemons = min(a, b // 2, c // 4)
total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
print(total_fruits)