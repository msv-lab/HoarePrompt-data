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
        
    #State of the program after the  for loop has been executed: Output State: The loop will execute as long as `n` is greater than or equal to `house_cost`. After the loop completes, the variable `a` will represent the number of houses purchased, `b` will represent the number of cars purchased such that the remaining amount is a multiple of `computer_cost`, and `remaining_after_cars` will be zero because the loop will ensure that any remaining amount after buying houses and cars is exactly divisible by `computer_cost`.
    #
    #Since the loop will continue to iterate until `remaining_after_cars` is zero and it is confirmed that this condition holds, the final values will be:
    #- `a`: The maximum integer such that `n - a * house_cost` is non-negative and `(n - a * house_cost) % car_cost` is non-negative and `(n - a * house_cost - b * car_cost) % computer_cost` is zero.
    #- `b`: The maximum integer such that `(n - a * house_cost - b * car_cost) % computer_cost` is zero.
    #- `remaining_after_cars`: 0, since the loop ensures that this value becomes zero before exiting.
    #
    #Therefore, the output state after the loop finishes executing is:
    #Output State: `a` is the maximum integer such that `n - a * house_cost` is non-negative and `(n - a * house_cost) % car_cost` is non-negative and `(n - a * house_cost - b * car_cost) % computer_cost` is zero, `b` is the maximum integer such that `(n - a * house_cost - b * car_cost) % computer_cost` is zero, and `remaining_after_cars` is 0.
    return 'NO'
    #'a' is the maximum integer such that `n - a * house_cost` is non-negative and `(n - a * house_cost) % car_cost` is non-negative and `(n - a * house_cost - b * car_cost) % computer_cost` is zero, 'b' is the maximum integer such that `(n - a * house_cost - b * car_cost) % computer_cost` is zero, and 'remaining_after_cars' is 0, 'NO'
#Overall this is what the function does:The function `func_1` accepts an integer `n` such that \(1 \leq n \leq 10^9\). It attempts to determine if it is possible to purchase a combination of houses, cars, and computers using exactly `n` units of currency. Each house costs `1234567` units, each car costs `123456` units, and each computer costs `1234` units. The function iterates over possible combinations of houses and cars to find if there exists a combination where the remaining amount of currency is exactly divisible by the cost of a computer. If such a combination is found, the function returns 'YES'. If no such combination is found, the function returns 'NO'.

