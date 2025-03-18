def func():
    t = int(input())
    for _ in range(t):
        (n, f, a, b) = map(int, input().split())
        arr = [0] + list(map(int, input().split()))
        possible = True
        for i in range(1, n + 1):
            time_diff = arr[i] - arr[i - 1]
            energy_keep_on = a * time_diff
            energy_turn_off_on = b
            energy_cost = min(energy_keep_on, energy_turn_off_on)
            if f <= energy_cost:
                possible = False
                break
            f -= energy_cost
        print('YES' if possible else 'NO')

