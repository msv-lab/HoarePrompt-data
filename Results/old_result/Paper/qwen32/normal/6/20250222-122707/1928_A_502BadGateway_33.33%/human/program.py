def solve(a, b):
    return "yes" if b % 2 == 0 else "no"
 
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solve(a, b))