#State of the program right berfore the function call: a, b, f, and k are integers such that 0 < f < a ≤ 10^6, 1 ≤ b ≤ 10^9, and 1 ≤ k ≤ 10^4.
def func():
    a, b, f, k = map(int, input().split())

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
        
    #State of the program after the  for loop has been executed: refuels is incremented for each insufficient fuel event, fuel is `b - 2 * (distance_to_fuel_station + distance_after_fuel_station) * (k // 2)` if no refuels, otherwise `b - 2 * (distance_to_fuel_station + distance_after_fuel_station) * (k // 2) - (number of refuels) * (b - distance_after_fuel_station)`, and current_position is `(current_position + total_distance) % (2 * a)`.
    print(refuels)
#Overall this is what the function does:The function processes a series of trips along a circular path of length \(2a\) where a vehicle starts with an initial fuel capacity \(b\). For each trip, the vehicle travels a distance of \(a\) and stops at either a fuel station located at distance \(f\) from the start or its opposite point. If the fuel is insufficient before reaching the fuel station, the vehicle must refuel to full capacity \(b\). The function calculates and prints the number of times the vehicle needs to refuel during \(k\) trips.

