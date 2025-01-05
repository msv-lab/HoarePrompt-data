#State of the program right berfore the function call: Stepan's integer is a string representation of a positive integer with a length between 2 and 200,000 digits, and m is a positive integer such that 2 ≤ m ≤ 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `Stepan's integer` is a string representation of a positive integer with a length between 2 and 200,000 digits; `a` is a positive integer; `b` is an input integer; `c` is the number of digits in the original value of `a`; `copya` is 0.
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
        
    #State of the program after the  for loop has been executed: `Stepan's integer` is a string representation of a positive integer, `a` is the modified integer after processing all digits, `ans` is the minimum of the results of `a % b` for all non-zero last digits in `a`.
    print(ans)
#Overall this is what the function does:The function accepts a string representation of a positive integer `a` with up to 200,000 digits and a positive integer `b` (2 ≤ b ≤ 10^8). It calculates and prints the minimum value of `a % b` by performing cyclic shifts of `a` while ignoring zero digits at the end, but it does not return any value or handle cases where `a` is less than `b`.

