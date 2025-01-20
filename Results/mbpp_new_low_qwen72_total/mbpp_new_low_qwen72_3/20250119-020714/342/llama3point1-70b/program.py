def mul_even_odd(nums):
    even = next((num for num in nums if num % 2 == 0), None)
    odd = next((num for num in nums if num % 2 != 0), None)
    return even * odd
