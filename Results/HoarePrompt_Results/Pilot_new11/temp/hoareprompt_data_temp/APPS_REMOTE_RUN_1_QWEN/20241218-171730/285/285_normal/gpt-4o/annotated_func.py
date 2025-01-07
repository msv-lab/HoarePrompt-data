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
        
    #State of the program after the  for loop has been executed: `a` is `n // house_cost`, `remaining_after_cars` is `n - (n // house_cost) * house_cost - ((n // house_cost) * (remaining_after_houses // car_cost + 1) - 1) * car_cost`. If the loop returned 'YES', then `remaining_after_cars % computer_cost == 0`. If not, `remaining_after_cars % computer_cost != 0`.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:Functionality: The function `func_1` accepts an integer `n` such that \(1 \leq n \leq 10^9\). It iterates through possible combinations of spending `n` units on houses, cars, and computers, checking if the remaining amount can be exactly divided by the cost of a computer. If such a combination is found, the function returns 'YES'. Otherwise, after exhausting all combinations, it returns 'NO'. The function considers all possible ways to spend up to `n` units on houses and cars before checking if the remaining amount can be exactly divided by the cost of a computer. Potential edge cases include when `n` is exactly divisible by the cost of a house, car, or computer, or when no valid combination is found.

