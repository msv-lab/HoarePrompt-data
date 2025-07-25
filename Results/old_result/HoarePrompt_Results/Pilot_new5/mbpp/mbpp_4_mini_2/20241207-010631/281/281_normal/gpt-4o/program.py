def Split(numbers):
    # Use a list comprehension to filter and return only even numbers
    return [num for num in numbers if num % 2 == 0]

# Test cases to validate the implementation
assert Split([1,2,3,4,5]) == [2, 4]
assert Split([4,5,6,7,8,0,1]) == [4, 6, 8, 0]
assert Split([8,12,15,19]) == [8, 12]
