def first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None
