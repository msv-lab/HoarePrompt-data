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
        
    #State of the program after the  for loop has been executed: refuels is 0 or 1, depending on whether fuel is less than distance_after_fuel_station at any point, fuel is either 0 (if refuels occurs) or the remaining fuel after all iterations, current_position is (current_position + k * a) % (2 * a), i is k - 1, distance_to_travel is a, distance_to_fuel_station alternates between f and a - f, distance_after_fuel_station alternates between a - f and f, k is the number of iterations, total_distance is 2 * a * k, and all other variables (a, b, f, current_position) remain as they were in the initial state.
    print(refuels)
#Overall this is what the function does:The function takes no explicit parameters but reads four integers \(a\), \(b\), \(f\), and \(k\) from standard input, where \(0 < f < a \leq 10^6\), \(1 \leq b \leq 10^9\), and \(1 \leq k \leq 10^4\). It simulates a vehicle traveling back and forth along a circular path of length \(2a\), starting with an initial fuel tank capacity of \(b\). For each iteration up to \(k\), the vehicle travels a distance \(a\) towards a fuel station located at a distance \(f\) from its current position, then refuels if necessary and continues its journey. If the vehicle cannot reach the fuel station without refueling, the function prints \(-1\) and exits immediately. After completing all iterations, the function prints the number of times the vehicle refueled. The final state of the program includes the number of refuels, the remaining fuel, and the current position of the vehicle on the circular path.

