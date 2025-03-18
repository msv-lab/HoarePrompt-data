#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \( n < (a + 1) \times 1234567 \), `house_cost` is 1234567, `car_cost` is 123456, `computer_cost` is 1234, `remaining_after_houses` is `n - a * 1234567`, `remaining_after_cars` is `remaining_after_houses - b * 123456` where `b` is the largest integer such that `remaining_after_cars >= 0` and `remaining_after_cars % 1234 != 0`. The program returns 'YES' if there exists an `a` and `b` such that `remaining_after_cars % 1234 == 0`, otherwise, the program returns 'NO'.
    return 'NO'
    #'NO'
#Overall this is what the function does:The function `func_1` accepts an integer `n` such that 1 ≤ n ≤ 10^9. It iterates through possible combinations of houses, cars, and computers that can be purchased with `n` units of currency, where each house costs 1234567 units, each car costs 123456 units, and each computer costs 1234 units. For each combination, it checks if the remaining amount of money after purchasing the houses and cars is exactly divisible by the cost of a computer. If such a combination exists, the function returns 'YES'. If no valid combination is found, the function returns 'NO'. The function does not handle cases where `n` is outside the specified range, returning 'NO' for any `n` that is not within 1 to 10^9 (inclusive).

