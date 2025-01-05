#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5.**
def func():
    n = int(input())
    i = '110'
    p = 1
    while int(i, 2) <= n:
        if n % int(i, 2) == 0:
            p = int(i, 2)
        
        i = '1' + i + '0'
        
    #State of the program after the loop has been executed: n is an input integer, i is '11111100', p is 1
    print(p)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, then iterates through binary numbers increasing in length until reaching a binary number greater than `n`. During this iteration, it checks if `n` is divisible by the binary representation of the current number. If it is divisible, it updates the variable `p` to that binary number. Finally, it prints the value of `p`. The function does not accept any parameters and does not return any values.

