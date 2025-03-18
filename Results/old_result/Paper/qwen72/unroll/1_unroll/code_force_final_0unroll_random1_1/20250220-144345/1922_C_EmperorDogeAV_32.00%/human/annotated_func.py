#State of the program right berfore the function call: cities is a list of n integers in strictly ascending order, where n is an integer such that 2 ≤ n ≤ 10^5, and each city's coordinate a_i satisfies 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9.
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
        
    #State: `prog_cities` is a list of n-1 integers where each element is either 1 or the distance to the next city in the list `cities`. The first element of `prog_cities` is always 1, and the last element of `prog_cities` is the distance between the second-to-last and last city in `cities`. All other elements are 1 if the distance to the next city is smaller than the distance to the previous city, otherwise, they are the distance to the next city.
    return prog_cities
    #The program returns the list `prog_cities` which contains n-1 integers. The first element of `prog_cities` is always 1, and the last element is the distance between the second-to-last and last city in the list `cities`. All other elements are 1 if the distance to the next city is smaller than the distance to the previous city, otherwise, they are the distance to the next city.
#Overall this is what the function does:The function `func_1` accepts two parameters: `cities`, a list of `n` integers in strictly ascending order, and `n`, an integer indicating the number of cities, where 2 ≤ n ≤ 10^5 and each city's coordinate a_i satisfies 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9. The function returns a list `prog_cities` containing `n-1` integers. The first element of `prog_cities` is always 1, and the last element is the distance between the second-to-last and last city in the list `cities`. For all other elements, they are 1 if the distance to the next city is smaller than the distance to the previous city, otherwise, they are the distance to the next city.

