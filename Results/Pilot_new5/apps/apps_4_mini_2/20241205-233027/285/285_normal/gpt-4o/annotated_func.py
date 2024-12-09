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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `house_cost` is 1234567, `car_cost` is 123456, `computer_cost` is 1234, `a` is `n // house_cost`, `remaining_after_houses` is `n - a * house_cost`, `b` is `remaining_after_houses // car_cost`, `remaining_after_cars` is `remaining_after_houses - b * car_cost`. If there is no combination found, the function does not return 'YES'.
    return 'NO'
    #The program returns 'NO' because there is no combination found based on the initial state variables.
#Overall this is what the function does:The function accepts a positive integer `n` and checks if it's possible to purchase a combination of houses, cars, and computers such that the total cost exactly matches `n`. It returns 'YES' if such a combination exists, otherwise it returns 'NO'. Specifically, it iterates through possible numbers of houses and cars, and checks if the remaining amount can be fully spent on computers. The function does not handle cases where `n` is less than the cost of a single computer; in those cases, it will return 'NO' without checking for combinations.

