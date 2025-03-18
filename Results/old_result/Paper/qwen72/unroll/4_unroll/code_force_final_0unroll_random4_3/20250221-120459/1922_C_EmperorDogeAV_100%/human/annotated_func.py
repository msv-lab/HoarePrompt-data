#State of the program right berfore the function call: cities is a list of n integers in strictly ascending order, where 2 ≤ n ≤ 10^5, and each city's coordinate a_i satisfies 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9.
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
        
    #State: `prog_cities` is a list of n-1 integers where each element is either 1 if the next city is closer than the previous city, or the distance to the next city if the next city is not closer than the previous city.
    return prog_cities
    #The program returns the list `prog_cities` which contains n-1 integers. Each integer in the list is either 1 if the next city is closer than the previous city, or the distance to the next city if the next city is not closer than the previous city.
#Overall this is what the function does:The function `func_1` accepts a list of city coordinates in strictly ascending order and an integer `n` representing the number of cities. It returns a list `prog_cities` of `n-1` integers. Each integer in the list is either `1` if the next city is closer than the previous city, or the distance to the next city if the next city is not closer than the previous city.

