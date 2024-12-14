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
        
    #State of the program after the  for loop has been executed: `n` is at least `1234567`, `house_cost` is `1234567`, `car_cost` is `123456`, `computer_cost` is `1234`, `remaining_after_houses` is equal to `n - a * house_cost` where `a` is at most `n // house_cost`, `b` is at most `remaining_after_houses // car_cost`, and if the inner loop executed, `remaining_after_cars` is equal to `remaining_after_houses - b * car_cost` where `remaining_after_cars % computer_cost` is `0`, meaning the function returned 'YES'. If no combination of `remaining_after_cars` made it divisible by `computer_cost`, the function will not return 'YES'. If the loops do not execute at all, then `remaining_after_houses` is equal to `n` and `remaining_after_cars` is equal to `n`.
    return 'NO'
    #The program returns 'NO', indicating that the combinations of `remaining_after_cars` do not yield a value divisible by `computer_cost`
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10^9) and checks if it's possible to buy a combination of houses, cars, and computers within the budget of `n`. Specifically, it attempts to find integers `a` and `b` such that the leftover funds after buying `a` houses and `b` cars is divisible by the cost of a computer. If such a combination exists, the function returns 'YES'; otherwise, it returns 'NO'. If `n` is less than the cost of a house, it will return 'NO' since it does not even allow for purchasing a house.

