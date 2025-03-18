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
        
    #State of the program after the  for loop has been executed: `a` is the maximum value of `a` for which the loop can execute, `b` is the maximum value of `b` for which the loop can execute, `remaining_after_houses` is the final value of `remaining_after_houses` after the loop ends, `remaining_after_cars` is the final value of `remaining_after_cars` after the loop ends, and `n` is the original value of `n`.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts an integer `n` between 1 and \(10^9\) (inclusive) and returns `'YES'` if it's possible to buy a combination of houses, cars, and computers such that the total cost exactly matches `n`. If no such combination exists, it returns `'NO'`.

