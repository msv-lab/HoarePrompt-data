#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 10^6.**
def func():
    n = int(input())
    x = int(n ** 0.5)
    if (x ** 2 == n) :
        answr = x * 4
    else :
        if (x * (x + 1) > n) :
            answr = (x + x + 1) * 2
        else :
            answr = 4 * (x + 1)
        #State of the program after the if-else block has been executed: *N is a positive integer such that 1 ≤ N ≤ 10^6, x is an integer representing the square root of N, the square of x is not equal to N. If x * (x + 1) > N, the function calculates 'answr' as described. Otherwise, if x * (x + 1) ≤ N, 'answr' is set to 4 * (x + 1)
    #State of the program after the if-else block has been executed: *N is a positive integer such that 1 ≤ N ≤ 10^6, x is an integer representing the square root of N. If the square of x is equal to N, 'answr' is 4 times the value of x. If the square of x is not equal to N and x * (x + 1) > N, 'answr' is calculated accordingly. If x * (x + 1) ≤ N, 'answr' is set to 4 * (x + 1)
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function takes user input for a positive integer N, calculates a value based on the square root of N, and prints the result. If the square of the square root of N is equal to N, the function calculates the result as 4 times the square root of N. If the square of the square root of N is not equal to N and x * (x + 1) is greater than N, the result is calculated accordingly. If x * (x + 1) is less than or equal to N, the result is set to 4 times (x + 1). The function does not accept any parameters and does not return any value.

