#State of the program right berfore the function call: Stepan's integer is a string of digits with a length between 2 and 200,000, inclusive, and does not contain leading zeros. m is an integer such that 2 ≤ m ≤ 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: Stepan's integer is a string of digits with a length between 2 and 200,000, inclusive, and does not contain leading zeros; `m` is an integer such that 2 ≤ `m` ≤ 10^8; `a` is a positive integer; `b` is an input integer; `c` is the number of digits in the original `a`; `copya` is 0.
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
        
    #State of the program after the  for loop has been executed: `m` is an integer such that 2 ≤ `m` ≤ 10^8; `copya` is 0; `ans` is the minimum value of `a % b` found during all iterations; `a` is modified based on the rearrangement of its digits.
    print(ans)
#Overall this is what the function does:The function accepts two integer inputs, `a` and `b`, where `a` is a positive integer and `b` is an integer between 2 and 10^8. The function calculates and prints the minimum value of `a % b` after attempting to rearrange the digits of `a`. It considers all possible arrangements by moving non-zero digits to the front, but only modifies `a` when the last digit is non-zero. If all digits are zero, the function does not handle this case explicitly, as it assumes that `a` will always be a valid positive integer input with no leading zeros.

