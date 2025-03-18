#State of the program right berfore the function call: cities is a list of n integers in strictly ascending order, where 2 ≤ n ≤ 10^5, and 0 ≤ cities[0] < cities[1] < ... < cities[n-1] ≤ 10^9.
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
        
    #State: `prog_cities` is a list of n-1 integers where each element is either 1 or the absolute difference between the current city and the next city, depending on which is smaller: the distance to the next city or the distance to the previous city. The list `cities` remains unchanged.
    return prog_cities
    #The program returns the list `prog_cities` which contains n-1 integers, where each integer is either 1 or the absolute difference between the current city and the next city, depending on which is smaller: the distance to the next city or the distance to the previous city. The list `cities` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts two parameters: `cities`, a list of integers in strictly ascending order, and `n`, an integer representing the number of cities in the list. It returns a new list `prog_cities` containing `n-1` integers. Each integer in `prog_cities` is either 1 or the absolute difference between the current city and the next city, depending on which is smaller: the distance to the next city or the distance to the previous city. The original list `cities` remains unchanged.

