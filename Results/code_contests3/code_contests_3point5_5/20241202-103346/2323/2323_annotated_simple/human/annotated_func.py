#State of the program right berfore the function call: The input consists of two positive integers, the first integer represents Stepan's very big positive integer and the second integer represents the number by which Stepan divides good shifts of his integer. The length of Stepan's integer is between 2 and 200,000 digits, and the second integer is between 2 and 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is a positive integer value (greater than or equal to 10), `b` is an input integer, `c` is the number of digits in the initial value of `a`, `copya` is 0
    ans = a % b
    for i in range(c):
        if a % 10 != 0:
            h = a % 10
            a //= 10
            a = 10 ** c * h + a
            ans = min(ans, a % b)
        else:
            h = a % 10
            a //= 10
            a = 10 ** c * h + a
        
    #State of the program after the  for loop has been executed: `a`, `b`, `c`, `copya`, `ans`, `i`, `h` are positive integers. The final value of `a` will be different based on the conditions met during the loop execution. The final value of `ans` will be the minimum remainder of the initial value of `a` divided by `b` after all iterations of the loop have finished.
    print(ans)
#Overall this is what the function does:The function `func` takes two positive integers as input: the first integer represents Stepan's very big positive integer, and the second integer represents the number by which Stepan divides good shifts of his integer. The function calculates the number of digits in the initial value of the first integer. Then, it iterates through each digit of the first integer, calculates a new value based on certain conditions, and finds the minimum remainder of the initial value of the first integer divided by the second integer. Finally, it prints the minimum remainder as the output. The function does not specify a return value. Edge cases to consider are: the length of Stepan's integer being between 2 and 200,000 digits, and the second integer being between 2 and 10^8.

