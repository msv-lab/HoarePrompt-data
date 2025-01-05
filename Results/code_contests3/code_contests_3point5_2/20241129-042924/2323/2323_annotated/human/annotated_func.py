#State of the program right berfore the function call: The input integer provided to Stepan is a positive integer without leading zeros. The integer m is a positive integer such that 2 ≤ m ≤ 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is the input integer, `b` is the input integer, `c` is the number of digits in the input integer `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: `a`, `b`, `c`, `copya`, `ans`, `i`, `h` are integers. The loop will not execute if `c` is less than or equal to 0. If the loop executes, `a` will be updated to a modified value based on the conditions inside the loop, `b` remains constant, `c` decreases by 1 after each iteration, `copya` remains 0, `ans` will hold the minimum value of `a % b` encountered during the loop iterations, `i` remains 0, and `h` holds the last digit of `a` at the end of the loop.
    print(ans)
#Overall this is what the function does:The function `func` reads two integer inputs `a` and `b`, calculates the number of digits in `a`, and then iterates through each digit of `a` to update its value based on certain conditions. Finally, it prints the minimum value of `a % b` encountered during the iterations. The function does not accept any parameters and focuses on integer manipulation based on the input values.

