#State of the program right berfore the function call: Stepan's integer is a positive integer with a length between 2 and 200,000 digits (inclusive) and does not contain leading zeros. The number m is an integer such that 2 ≤ m ≤ 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: Stepan's integer is a positive integer, m is an integer between 2 and 10^8, a is an input integer not equal to 0, b is an input integer, c is the number of digits in Stepan's integer, copya is 0
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, Stepan's integer is a positive integer, `m` is an integer between 2 and 10^8, `a` is an integer after all divisions, `b` is an input integer, `c` is the number of digits in Stepan's integer, `copya` is 0, `ans` is the final minimum value after all iterations, `h` is the last digit of the final `a`.
    print(ans)
#Overall this is what the function does:The function accepts two integer inputs, `a` and `b`, calculates the remainder of `a` divided by `b`, and prints the minimum remainder obtained by cyclically shifting the digits of `a`. The number of digits in `a` is determined by the variable `c`.

