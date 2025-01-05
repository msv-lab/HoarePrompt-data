#State of the program right berfore the function call: The input consists of two positive integers, the first one representing Stepan's integer and the second one representing the number m for division. The length of Stepan's integer is between 2 and 200,000 digits, and m is such that 2 <= m <= 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `c` is 3, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: `c` is 3, `copya` is 0, `ans` is the minimum value of the remainders of `a` divided by `b` after each iteration of the loop.
    print(ans)
#Overall this is what the function does:The function `func` takes two positive integers as input: Stepan's integer and the number `m` for division. Stepan's integer has a length between 2 and 200,000 digits, and `m` is within the range 2 <= m <= 10^8. The function calculates the minimum remainder of the division of Stepan's integer `a` by `b` after specific operations. The function then prints the calculated minimum remainder `ans`.

