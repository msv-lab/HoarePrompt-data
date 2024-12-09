def func_1(numbers):
    rounded_numbers = [round(num) for num in numbers]
    total_sum = sum(rounded_numbers)
    result = total_sum * len(numbers)
    return result
assert func_1([22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]) == 243
assert func_1([5, 2, 9, 24.3, 29]) == 345
assert func_1([25.0, 56.7, 89.2]) == 513