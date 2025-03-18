#State of the program right berfore the function call: n is a positive integer representing the number of bus routes, t is a positive integer representing the time Serval goes to the station, and bus_routes is a list of tuples where each tuple contains two positive integers representing the time when the first bus of the route arrives and the interval between two buses of that route.**
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
        
    #State of the program after the  for loop has been executed: n and t are positive integers. bus_routes is a list of tuples where each tuple contains two positive integers. min_wait_time is equal to the minimum wait time calculated across all routes. chosen_route is the index of the route with the minimum wait time + 1.
    return chosen_route
    #The program returns the index of the route with the minimum wait time + 1
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `t`, and `bus_routes`. `n` is a positive integer representing the number of bus routes, `t` is a positive integer representing the time Serval goes to the station, and `bus_routes` is a list of tuples where each tuple contains two positive integers representing the time when the first bus of the route arrives and the interval between two buses of that route. The function calculates the minimum wait time for each bus route based on Serval's time and returns the index of the route with the minimum wait time + 1. If there are multiple routes with the same minimum wait time, the function will choose the first encountered route.

