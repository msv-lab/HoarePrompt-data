def diff_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    first_even = even_numbers[0]
    first_odd = odd_numbers[0]
    return abs(first_even - first_odd)
