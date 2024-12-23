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
    return 'NO'
n = int(input().strip())
result = func_1(n)
print(result)