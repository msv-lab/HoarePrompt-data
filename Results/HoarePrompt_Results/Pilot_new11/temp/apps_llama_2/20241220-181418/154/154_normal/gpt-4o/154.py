def max_points(n, k, M, t):
    # Calculate total time required to solve all subtasks of one task
    total_time_per_task = sum(t)
    
    max_points = 0
    
    # Try solving 0 to n tasks completely
    for complete_tasks in range(n + 1):
        time_used = complete_tasks * total_time_per_task
        if time_used > M:
            break
        
        # Points for completely solved tasks
        points = complete_tasks * (k + 1)
        
        # Remaining time to solve individual subtasks
        remaining_time = M - time_used
        
        # Solve as many individual subtasks as possible with the remaining time
        subtasks_solved = 0
        for subtask_time in t:
            if remaining_time >= subtask_time:
                max_subtasks_for_this_task = (remaining_time // subtask_time)
                subtasks_solved += max_subtasks_for_this_task
                remaining_time -= max_subtasks_for_this_task * subtask_time
        
        # Ensure not to count more subtasks than available
        subtasks_solved = min(subtasks_solved, (n - complete_tasks) * k)
        
        # Update max points
        max_points = max(max_points, points + subtasks_solved)
    
    return max_points

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
M = int(data[2])
t = list(map(int, data[3:3+k]))

# Get the result and print it
result = max_points(n, k, M, t)
print(result)
