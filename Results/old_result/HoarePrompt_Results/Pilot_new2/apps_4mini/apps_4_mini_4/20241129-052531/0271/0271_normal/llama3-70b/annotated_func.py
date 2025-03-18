#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.
def func():
    n = int(input())
    if (n % 10 == 0) :
        print(n)
    else :
        if (n % 10 <= 5) :
            print(n - n % 10)
        else :
            print(n + (10 - n % 10))
        #State of the program after the if-else block has been executed: *`n` is an integer satisfying 0 ≤ n ≤ 10^9 and is not a multiple of 10. If `n % 10` is less than or equal to 5, `n` is updated to the largest multiple of 10 that is less than or equal to its previous value. Otherwise, if `n % 10` is greater than 5, the result printed is either `n + 4`, `n + 3`, `n + 2`, or `n + 1`.
    #State of the program after the if-else block has been executed: *`n` is an integer satisfying 0 ≤ n ≤ 10^9. If `n` is divisible by 10, its value is printed to the console. If `n` is not a multiple of 10 and `n % 10` is less than or equal to 5, `n` is updated to the largest multiple of 10 that is less than or equal to its previous value. If `n % 10` is greater than 5, the printed result is either `n + 4`, `n + 3`, `n + 2`, or `n + 1`.
#Overall this is what the function does:The function accepts a non-negative integer input from the user and prints it if it is a multiple of 10. If the input is not a multiple of 10, it prints the largest multiple of 10 that is less than or equal to the input if the remainder when divided by 10 is less than or equal to 5. If the remainder is greater than 5, it prints the next higher multiple of 10. The function does not return any value; it only prints to the console.

