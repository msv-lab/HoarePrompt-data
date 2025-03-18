#State of the program right berfore the function call: cities is a list of n integers in strictly ascending order, where 2 ≤ n ≤ 10^5, and 0 ≤ cities[i] ≤ 10^9 for all 0 ≤ i < n.
def func_1(cities, n):
    prog_cities = [0] * (n - 1)
    for i in range(n - 1):
        back = -99999999999999999999
        
        forward = 999999999999999999
        
        if i > 0:
            back = cities[i - 1]
        
        if i < n - 1:
            forward = cities[i + 1]
        
        if abs(forward - cities[i]) < abs(cities[i] - back):
            prog_cities[i] = 1
        else:
            prog_cities[i] = abs(forward - cities[i])
        
    #State: `cities` is a list of n integers in strictly ascending order, `prog_cities` is a list of n-1 integers where each element at index i is either 1 if the city at index i+1 is closer to the city at index i than the city at index i-1, or the absolute difference between the city at index i+1 and the city at index i otherwise. The loop has completed all iterations, and `i` is equal to `n - 1`.
    return prog_cities
    #The program returns `prog_cities`, a list of n-1 integers where each element at index i is either 1 if the city at index i+1 is closer to the city at index i than the city at index i-1, or the absolute difference between the city at index i+1 and the city at index i otherwise.
#Overall this is what the function does:The function `func_1` accepts two parameters: `cities`, a list of `n` integers in strictly ascending order, and `n`, an integer representing the number of cities. It returns a list `prog_cities` of `n-1` integers. Each element at index `i` in `prog_cities` is either 1 if the city at index `i+1` in `cities` is closer to the city at index `i` than the city at index `i-1`, or the absolute difference between the city at index `i+1` and the city at index `i` otherwise. The original `cities` list remains unchanged.

