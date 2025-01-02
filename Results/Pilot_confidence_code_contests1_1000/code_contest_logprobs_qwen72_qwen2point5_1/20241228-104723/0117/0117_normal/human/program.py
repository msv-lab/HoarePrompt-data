[n,k, M] = [int(i) for i in raw_input().split(' ')]
times = [int(i) for i in raw_input().split(' ')]
times.sort()
times_matrix = [times for i in range(n)]

best_points = 0
#Iterate by gradually increasing starting row
for start_row in range(0, n):
    total_time = sum(times) * start_row
    total_points = (k + 1) * start_row
    [cur_row, cur_col] = [start_row,0]
    #sum vertically, moving down column, then moving columns
    while total_time <= M and cur_col < k:
        if cur_row >= n:
            cur_row = start_row
            cur_col += 1
        else:
            if total_time + times_matrix[cur_row][cur_col] > M:
                break
            else:
                total_time += times_matrix[cur_row][cur_col]
                cur_row += 1
                total_points += 1
    if best_points < total_points and total_time <= M:
        best_points = total_points

print(best_points)
