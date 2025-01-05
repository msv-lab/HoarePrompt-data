#State of the program right berfore the function call: Stepan's integer is a positive integer without leading zeros. The number m is an integer such that 2 ≤ m ≤ 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is a non-zero positive integer, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: Output State: `a`, `b`, `c`, `copya`, `ans`, `h` are integers. The loop will execute `c` times in total. After the loop finishes, `a` will be 0, `copya` will be the original value of `a`, `ans` will be the minimum remainder of `a` divided by `b` for all iterations, `h` will be the last digit of the original `a`.
    print(ans)
#Overall this is what the function does:The function `func` takes two input integers `a` and `b`. It calculates the number of digits in `a` and then iterates through each digit to update `a` accordingly. The function then finds the minimum remainder of `a` divided by `b` for all iterations and prints this value.

