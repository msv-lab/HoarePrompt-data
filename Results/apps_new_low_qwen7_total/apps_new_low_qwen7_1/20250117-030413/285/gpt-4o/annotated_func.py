#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func_1(n):
    house_cost = 1234567

car_cost = 123456

computer_cost = 1234
    for a in range(n // house_cost + 1):
        remaining_after_houses = n - a * house_cost
        
        for b in range(remaining_after_houses // car_cost + 1):
            remaining_after_cars = remaining_after_houses - b * car_cost
            if remaining_after_cars % computer_cost == 0:
                return 'YES'
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than 0 and a multiple of 123456, `house_cost` is 1234567, `car_cost` is 123456, `computer_cost` is 1234, `a` is `n // house_cost`, `remaining_after_houses` is 0, `b` is the number of iterations performed by the inner loop, and the function returns 'YES' if `remaining_after_houses` can be reduced to 0 by the inner loop and `remaining_after_cars % computer_cost == 0`. Otherwise, the function returns nothing.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts an integer `n` where \(1 \leq n \leq 10^9\). It iterates over possible combinations of houses, cars, and computers that can be purchased with `n` units of currency, given their respective costs (`house_cost`, `car_cost`, and `computer_cost`). If it finds a combination where the remaining amount can be exactly divided by the cost of a computer (`computer_cost`), it returns 'YES'. Otherwise, after completing all iterations, it returns 'NO'.

