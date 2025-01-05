#State of the program right berfore the function call: The first input is a string representing a positive integer with a length between 2 and 200,000 digits, and the second input is an integer m (2 ≤ m ≤ 10^8).
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `copya` is 0, `c` is the number of digits in the original value of `a`, `a` is a positive integer input, `b` is an input integer.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `c` is greater than 0, `ans` is the minimum remainder of the modified `a` divided by `b` after all digits of `a` have been processed, and `a` is a positive integer formed by rearranging its digits.
    print(ans)
#Overall this is what the function does:The function accepts a string representation of a positive integer `a` (with a length between 2 and 200,000 digits) and an integer `b` (where 2 ≤ b ≤ 10^8). It calculates the minimum remainder of `a` when divided by `b` after potentially rearranging the digits of `a` by moving non-zero digits to the front. The function outputs this minimum remainder. If `a` is modified by moving its digits, the function ensures that zeros are not moved to the front, which could change the value.

