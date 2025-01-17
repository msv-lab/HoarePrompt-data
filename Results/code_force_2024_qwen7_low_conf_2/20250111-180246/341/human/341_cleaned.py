def func_1(n, lecturers):
    max_day = 200000
    availability = [0] * (max_day + 2)
    for (l, r) in lecturers:
        availability[l] += 1
        availability[r + 1] -= 1
    current_available = 0
    available_days = [0] * (max_day + 1)
    for day in range(1, max_day + 1):
        current_available += availability[day]
        available_days[day] = current_available
    result = [0] * (n + 1)
    for k in range(1, n + 1):
        count = 0
        current_window_sum = sum(available_days[1:k + 1])
        if current_window_sum >= k:
            count += 1
        for start in range(2, max_day - k + 2):
            current_window_sum += available_days[start + k - 1] - available_days[start - 1]
            if current_window_sum >= k:
                count += 1
        result[k] = count
    return result[1:]
input = sys.stdin.read
data = input().split()
n = int(data[0])
lecturers = []
index = 1
for _ in range(n):
    l = int(data[index])
    r = int(data[index + 1])
    lecturers.append((l, r))
    index += 2
result = func_1(n, lecturers)
print(' '.join(map(str, result)))