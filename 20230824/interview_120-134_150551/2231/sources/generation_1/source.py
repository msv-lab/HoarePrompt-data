T = int(input())

for _ in range(T):
    n = int(input())
    sticks = list(map(int, input().split()))

    sticks.sort()

    min_value = float('inf')
    result = []

    for i in range(n - 3):
        area = sticks[i] * sticks[i + 2]
        perimeter = 2 * (sticks[i] + sticks[i + 2])
        value = (perimeter**2) / area

        if value < min_value:
            min_value = value
            result = [sticks[i], sticks[i], sticks[i + 2], sticks[i + 2]]

    print(*result)