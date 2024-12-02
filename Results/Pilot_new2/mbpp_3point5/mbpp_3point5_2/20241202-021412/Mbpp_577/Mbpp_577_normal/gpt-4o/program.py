def last_Digit_Factorial(n):
    if n >= 5:
        return 0
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial % 10

# Testing the function
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(21) == 0
assert last_Digit_Factorial(30) == 0
