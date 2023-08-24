T = int(input())

for _ in range(T):
    n = int(input())
    sticks = list(map(int, input().split()))

    sticks.sort()

    min_value = float('inf')
    result = []

    for i in range(n - 3):
        for j in range(i + 1, n - 2):  # Fix: iterate over the remaining sticks
            area = sticks[i] * sticks[j]  # Fix: calculate the area correctly
            perimeter = 2 * (sticks[i] + sticks[j])
            value = (perimeter**2) / area

            if value < min_value:
                min_value = value
                result = [sticks[i], sticks[i + 1], sticks[j], sticks[j + 1]]  # Fix: update the result correctly

    print(*result)