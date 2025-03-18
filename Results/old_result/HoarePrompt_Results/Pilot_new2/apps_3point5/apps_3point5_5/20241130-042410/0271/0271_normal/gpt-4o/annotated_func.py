#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.**
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *n is a non-negative integer with a value assigned from input, remainder is an integer ranging from 0 to 9 based on the calculation n % 10. If remainder is less than or equal to 5, the result will be n - remainder. If remainder is larger than 5, the result will be n + (10 - remainder).
    print(result)
#Overall this is what the function does:The function reads an integer input n, calculates the remainder of n divided by 10, and based on the value of the remainder, it calculates a result. If the remainder is less than or equal to 5, the result is n minus the remainder; otherwise, the result is n plus the difference between 10 and the remainder. The function then prints the result. The function does not accept any parameters and does not return any output.

