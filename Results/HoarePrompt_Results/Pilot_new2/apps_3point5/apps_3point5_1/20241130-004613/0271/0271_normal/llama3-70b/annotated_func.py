#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = int(input())
    if (n % 10 == 0) :
        print(n)
    else :
        if (n % 10 <= 5) :
            print(n - n % 10)
        else :
            print(n + (10 - n % 10))
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `n` is assigned the value of int(input()). `n` is not divisible by 10. If `n % 10` is less than or equal to 5, the value printed is the result of `n - n % 10`. If `n % 10` is larger than 5, the value printed is `10`.
    #State of the program after the if-else block has been executed: *n is a non-negative integer. If n is divisible by 10 with a remainder of 0, the value of n is printed. If n is not divisible by 10, the value printed is based on the value of n % 10. If n % 10 is less than or equal to 5, the printed value is n - n % 10. If n % 10 is greater than 5, the printed value is 10.
#Overall this is what the function does:The function `func` reads an integer input `n` from the user. If `n` is divisible by 10, it prints the value of `n`. If `n` is not divisible by 10, it adjusts the value based on the remainder of `n % 10`. If the remainder is less than or equal to 5, it prints `n - n % 10`. If the remainder is greater than 5, it prints `n + (10 - n % 10)`. The function does not accept any parameters and does not return any value.

