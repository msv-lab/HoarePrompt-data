#State of the program right berfore the function call: the input consists of a string representing a positive integer with a length between 2 and 200,000 digits, and an integer m (2 ≤ m ≤ 10^8).
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `copya` is 0, `c` is the number of digits in the original value of `a`, `a` is a positive integer, `b` is an input integer.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `c` is the number of digits in the original value of `a`, `ans` is the minimum remainder of the modified `a` divided by `b`, `a` is reduced to a value based on its digits, and `b` is an input integer.
    print(ans)
#Overall this is what the function does:The function accepts two inputs: a positive integer `a` and an integer `b`. It calculates the minimum remainder of `a` when divided by `b` after modifying `a` by rotating its digits. The function considers all possible rotations of the digits of `a` (leftmost non-zero digit to the front) and finds the minimum remainder when each modified version of `a` is divided by `b`. The result is printed as output.

