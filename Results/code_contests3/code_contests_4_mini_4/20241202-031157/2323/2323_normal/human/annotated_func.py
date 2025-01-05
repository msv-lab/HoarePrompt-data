#State of the program right berfore the function call: Stepan's integer is represented as a string of digits with length between 2 and 200,000, inclusive, and does not contain leading zeros. m is an integer such that 2 ≤ m ≤ 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: Stepan's integer is a string of digits with length between 2 and 200,000; `m` is an integer such that 2 ≤ `m` ≤ 10^8; `a` is greater than 0; `b` is an input integer; `c` is equal to the number of digits in the original value of `a`; `copya` is 0.
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
        
    #State of the program after the  for loop has been executed: `Stepan's integer` is a string of digits with length between 2 and 200,000; `m` is an integer such that 2 ≤ `m` ≤ 10^8; `a` is a rearranged integer formed from the digits of the original `a`, `c` is 0, `copya` is 0, `ans` is the minimum remainder of all rearrangements of `a` when divided by `b`, and `i` is equal to the length of the original `a`.
    print(ans)
#Overall this is what the function does:The function accepts two integer inputs, `a` and `b`, where `a` is a large integer represented as a string of digits and `b` is an integer (2 ≤ b ≤ 10^8). It calculates the minimum remainder of all rearrangements of the digits of `a` when divided by `b` and prints this minimum remainder. It does not check if `a` is divisible by `m` nor does it return "Yes" or "No" based on divisibility.

