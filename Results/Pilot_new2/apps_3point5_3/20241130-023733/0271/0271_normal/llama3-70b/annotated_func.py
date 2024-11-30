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
        #State of the program after the if-else block has been executed: *`n` is an integer not divisible by 10. If `n % 10 <= 5`, the program prints `n - n % 10`, which removes the last digit of `n`. If `n % 10 > 5`, the program prints `n + (10 - n % 10)`.
    #State of the program after the if-else block has been executed: *`n` is an integer. If `n % 10 == 0`, the program prints the value of `n`. If `n % 10 <= 5`, the program prints `n - n % 10`, removing the last digit of `n`. If `n % 10 > 5`, the program prints `n + (10 - n % 10)`.
#Overall this is what the function does:The function `func` reads an integer from the user input and performs different operations based on the value of the integer. If the integer is divisible by 10, it prints the integer itself. If the integer is not divisible by 10, it rounds the integer down to the nearest multiple of 10 if the last digit is less than or equal to 5, otherwise, it rounds the integer up to the nearest multiple of 10. The function does not accept any parameters and does not return any value.

