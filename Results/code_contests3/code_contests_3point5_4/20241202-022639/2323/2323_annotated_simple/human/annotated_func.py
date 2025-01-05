#State of the program right berfore the function call: **
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is an input integer, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: `a`, `b`, `c-1`, `copya`, `ans`, `h` are integers. The final value of `a` is the updated value after the loop finishes executing, `b` remains the same, `c` is the number of digits in the original value of `a` minus the number of times the loop executed, `copya` is 0, `ans` is the minimum value of the remainder of `a` divided by `b` after all iterations, `h` is the last digit of the final value of `a`.
    print(ans)
#Overall this is what the function does:The function reads two integer inputs a and b, calculates the number of digits in a, finds the minimum remainder of a divided by b after modifying a, and prints the final result. The function does not accept any parameters and does not have explicit return values.

