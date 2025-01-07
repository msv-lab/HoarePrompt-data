def func_1(n, k, M, t):
    total_time_per_task = sum(t)
    max_points = 0
    for complete_tasks in range(n + 1):
        time_used = complete_tasks * total_time_per_task
        if time_used > M:
            break
        points = complete_tasks * (k + 1)
        remaining_time = M - time_used
        subtasks_solved = 0
        for subtask_time in t:
            if remaining_time >= subtask_time:
                max_subtasks_for_this_task = remaining_time // subtask_time
                subtasks_solved += max_subtasks_for_this_task
                remaining_time -= max_subtasks_for_this_task * subtask_time
        subtasks_solved = min(subtasks_solved, (n - complete_tasks) * k)
        max_points = max(max_points, points + subtasks_solved)
    return max_points
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
M = int(data[2])
t = list(map(int, data[3:3 + k]))
result = func_1(n, k, M, t)
print(result)