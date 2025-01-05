def is_beautiful_array(n, a):
    x = min(a)

    b = [num for num in a if num % x != 0]

    if not b:
        return "Yes"

    y = min(b)
    for num in b:
        if num % y != 0:
            return "No"

    return "Yes"

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(is_beautiful_array(n, a))

print("\n".join(results))
