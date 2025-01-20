(a, b, f, k) = map(int, input().split())
refuels = 0
fuel = b
total_distance = 2 * a * k
current_position = 0
for i in range(k):
    if i % 2 == 0:
        distance_to_travel = a
        distance_to_fuel_station = f
        distance_after_fuel_station = a - f
    else:
        distance_to_travel = a
        distance_to_fuel_station = a - f
        distance_after_fuel_station = f
    if fuel < distance_to_fuel_station:
        print(-1)
        exit()
    fuel -= distance_to_fuel_station
    if fuel < distance_after_fuel_station:
        refuels += 1
        fuel = b
    fuel -= distance_after_fuel_station
    current_position = (current_position + distance_to_travel) % (2 * a)
print(refuels)