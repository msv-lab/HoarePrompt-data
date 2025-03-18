#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that `1 ≤ n ≤ 10^9`, `a` is the maximum number of houses that can be purchased, `remaining_after_houses` is equal to `n - a * house_cost`, `b` is the maximum number of cars that can be purchased for each `a`, and `remaining_after_cars` is the remaining amount after purchasing `a` houses and `b` cars; if no valid combination results in `remaining_after_cars` being divisible by `computer_cost`, the program does not return 'YES'.
    return 'NO'
    #The program returns 'NO' indicating that there is no valid combination of houses and cars such that the remaining amount is divisible by computer_cost.
#Overall this is what the function does:The function accepts a positive integer `n` and determines if it is possible to buy a combination of houses (costing 1,234,567 each) and cars (costing 123,456 each) such that the remaining amount after these purchases is divisible by the cost of a computer (1,234). It returns 'YES' if such a combination exists, otherwise, it returns 'NO'.

