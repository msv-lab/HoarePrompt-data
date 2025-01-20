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
        
    #State of the program after the  for loop has been executed: n is 0, 'YES' is returned.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts an integer `n` where \(1 \leq n \leq 10^9\). It iterates over possible combinations of spending `n` on houses, cars, and computers, checking if the remaining amount can be evenly divided by the cost of a computer. If such a combination is found, the function returns `'YES'`. Otherwise, it returns `'NO'`. Specifically, the function will return `'NO'` only when no valid combination of spending on houses, cars, and computers leaves a remainder divisible by the cost of a computer.

