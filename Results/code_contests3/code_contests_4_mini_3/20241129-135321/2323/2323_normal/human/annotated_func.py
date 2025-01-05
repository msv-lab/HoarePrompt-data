#State of the program right berfore the function call: stepan_integer is a string representing a positive integer of length between 2 and 200,000 digits without leading zeros, and m is an integer such that 2 <= m <= 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `stepan_integer` is a string representing a positive integer of length between 2 and 200,000 digits without leading zeros; `m` is an integer such that 2 <= m <= 10^8; `a` is greater than or equal to 10; `b` is an input integer; `c` is the number of digits in the original value of `a`; `copya` is 0.
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
        
    #State of the program after the  for loop has been executed: `stepan_integer` is a string representing a positive integer of length between 2 and 200,000 digits without leading zeros; `m` is an integer such that 2 <= m <= 10^8; `a` is a number resulting from the transformation of the original value of `a`; `ans` is the minimum of its original value and `a % b`.
    print(ans)
#Overall this is what the function does:The function accepts two input integers, `a` and `b`, where `a` is expected to be a positive integer with at least 2 digits, and `b` is an integer such that 2 <= b <= 10^8. It computes the minimum value of `a % b` after transforming `a` by moving its last non-zero digit to the front, and prints this minimum value. The function does not handle cases where `a` has no non-zero digits.

