#State of the program right berfore the function call: cities is a list of n integers in strictly ascending order (0 <= cities[0] < cities[1] < ... < cities[n-1] <= 10^9), and n is an integer such that 2 <= n <= 10^5.
def func_1(cities, n):
    prog_cities = [0] * (n - 1)
    for i in range(n - 1):
        back = -99999999
        
        forward = 99999999
        
        if i > 0:
            back = cities[i - 1]
        
        if i < n - 1:
            forward = cities[i + 1]
        
        if abs(forward - cities[i]) < abs(cities[i] - back):
            prog_cities[i] = 1
        else:
            prog_cities[i] = abs(forward - cities[i])
        
    #State: `prog_cities` is a list of n-1 integers where each element is either 1 or the absolute difference between the current city and the previous city, depending on the distance to the next city being less than the distance to the previous city.
    return prog_cities
    #The program returns the list `prog_cities` which contains n-1 integers, where each integer is either 1 or the absolute difference between the current city and the previous city, depending on the distance to the next city being less than the distance to the previous city.
#Overall this is what the function does:The function `func_1` accepts a list `cities` of `n` integers in strictly ascending order and an integer `n` (2 <= n <= 10^5). It returns a list `prog_cities` of `n-1` integers. Each element in `prog_cities` is either 1 or the absolute difference between the current city and the next city, depending on whether the distance to the next city is less than the distance to the previous city. If the distance to the next city is less, the element is 1; otherwise, it is the absolute difference between the current city and the previous city.

