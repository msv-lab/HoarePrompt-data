#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    divisors_sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i != n:
                divisors_sum += i + n // i
            else:
                divisors_sum += i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` has iterated from 1 to `int(n
    return divisors_sum - n
    #The program returns the value of `divisors_sum - n`, where `divisors_sum` is the sum of all divisors of `n` (excluding `n` itself) that were found during the iteration from 1 to `int(n)`
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and returns the sum of all proper divisors of `n` (excluding `n` itself). A proper divisor of `n` is any number that divides `n` without leaving a remainder, excluding `n` itself. The function correctly handles the case where `n` is a perfect square by ensuring that the square root is only added once to the sum. If `n` is 1, the function returns 0, as 1 has no proper divisors.

#State of the program right berfore the function call: n is a positive integer.
def func_2(n):
    amicable_sum = 0
    for num in range(1, n + 1):
        if func_1(num) < n:
            if func_1(func_1(num)) == num and num != func_1(num):
                amicable_sum += num
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, and `amicable_sum` is the sum of all `num` values from 1 to `n` that satisfy the conditions `func_1(num) < n`, `func_1(func_1(num)) == num`, and `num != func_1(num)`.
    return amicable_sum
    #The program returns the sum of all `num` values from 1 to `n` that satisfy the conditions `func_1(num) < n`, `func_1(func_1(num)) == num`, and `num != func_1(num)`.
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` and returns the sum of all integers `num` from 1 to `n` that satisfy the following conditions: `func_1(num) < n`, `func_1(func_1(num)) == num`, and `num != func_1(num)`. If no such numbers exist within the range, the function returns 0. The function does not modify the input `n` and only computes and returns the sum based on the specified conditions.

