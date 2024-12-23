def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product / len(numbers)