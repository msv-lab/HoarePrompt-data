def calculate_earliest_start_time(scheduled_trains, num_stations):
    earliest_start_time = float('inf')
    for train in scheduled_trains:
        delay = train[3]
        for station in range(1, num_stations):
            planned_departure = train[1] + (station - 1) * train[3]
            planned_arrival = train[2] + (station - 1) * train[3]
            earliest_start = planned_arrival - delay
            earliest_start_time = max(earliest_start_time, earliest_start)
    if earliest_start_time >= 86400:
        return "impossible"
    else:
        return earliest_start_time

N, M = map(int, input().split())
scheduled_trains = []
for _ in range(M):
    train = list(map(int, input().split()))
    scheduled_trains.append(train)

earliest_start = calculate_earliest_start_time(scheduled_trains, N)
print(earliest_start)