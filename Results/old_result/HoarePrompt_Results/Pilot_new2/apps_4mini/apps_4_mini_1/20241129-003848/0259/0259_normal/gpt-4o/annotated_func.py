#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, t is a positive integer such that 1 <= t <= 10^5, and bus_routes is a list of tuples where each tuple contains two positive integers (s_i, d_i) such that 1 <= s_i, d_i <= 10^5.
def func_1(n, t, bus_routes):
    min_wait_time = float('inf')
    chosen_route = -1
    for i in range(n):
        s_i, d_i = bus_routes[i]
        
        if s_i >= t:
            wait_time = s_i - t
        elif (t - s_i) % d_i == 0:
            wait_time = 0
        else:
            wait_time = d_i - (t - s_i) % d_i
        
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            chosen_route = i + 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= n <= 100; `t` is a positive integer such that 1 <= t <= 10^5; `bus_routes` is a list of tuples containing positive integers; `min_wait_time` is the minimum wait time calculated based on the bus routes; `chosen_route` is the index (1-based) of the bus route that offers the minimum wait time. If no suitable route is found, `min_wait_time` remains float('inf') and `chosen_route` remains -1.
    return chosen_route
    #The program returns the index (1-based) of the bus route that offers the minimum wait time, or -1 if no suitable route is found.
#Overall this is what the function does:The function accepts a positive integer `n` (the number of bus routes), a positive integer `t` (the current time), and a list of tuples `bus_routes`, each containing two positive integers representing the start time and interval of the bus routes. It calculates the minimum wait time for a bus route and returns the index (1-based) of the bus route that offers the minimum wait time. If no suitable bus route is found (i.e., all buses start after time `t`), it returns -1.

