#State of the program right berfore the function call: n is an integer such that 1 <= n <= 105.**
def func():
    n = int(input())
    i = '110'
    p = 1
    while int(i, 2) <= n:
        if n % int(i, 2) == 0:
            p = int(i, 2)
        
        i = '1' + i + '0'
        
    #State of the program after the loop has been executed: n` is an input integer, `i` in binary form has been adjusted so that its integer value is greater than `n`, `p` is the integer value of the previous `i` in binary form
    print(p)
#Overall this is what the function does:The function `func` reads an integer `n` as input and iteratively updates a binary string `i` until its integer value exceeds `n`. During this process, it checks if `n` is divisible by the integer value of `i` in binary form and updates the variable `p` accordingly. Finally, it prints the value of `p`. The function does not accept any parameters explicitly, but it operates based on user input within the specified constraints.

