#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer, `s` is 1 if `n` is not divisible by 10. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` reads an input integer `n` and checks if it is divisible by 10. If `n` is not divisible by 10, it sets `s` to 1; otherwise, `s` remains 0. Then, it calculates 2 times `n` divided by 10 plus `s` and prints the result. The function does not accept any parameters explicitly. However, it implicitly expects the user to input a non-negative integer `n`.

