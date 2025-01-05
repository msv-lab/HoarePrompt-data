#State of the program right berfore the function call: The input integer is a string representing a positive integer with a length between 2 and 200,000 digits, and the integer m is an integer such that 2 ≤ m ≤ 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `copya` is 0, `c` is the number of digits in the original value of `a`, `a` is the input integer converted from the string representation of a positive integer, `b` is an input integer.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `c` is greater than 0, `i` is equal to `c`, `a` is the rearranged value of the original `a`, `ans` is the minimum of its initial value and the last computed value of `a % b`.
    print(ans)
#Overall this is what the function does:The function accepts two inputs: a positive integer `a` (provided as a string) and an integer `b` (where 2 ≤ b ≤ 10^8). It calculates the minimum value of `a % b` by examining all possible single-digit rotations of `a` (by moving the last digit to the front) and prints this minimum value. If `a` consists of digits that all eventually lead to a zero when rotated, it may not explore all valid configurations, but it will still handle cases where the last digit is zero correctly. The function does not explicitly handle input validation for the string representation's conformity to being a positive integer or for the range of `b`.

