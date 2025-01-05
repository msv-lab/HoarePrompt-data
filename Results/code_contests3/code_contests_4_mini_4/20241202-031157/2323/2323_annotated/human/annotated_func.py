#State of the program right berfore the function call: the input consists of a string representing a positive integer of length between 2 and 200,000 digits without leading zeros, followed by an integer m where 2 ≤ m ≤ 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `copya` is 0, `c` is the number of digits in the original value of `a`, `a` is a positive integer, `b` is an input integer converted from a string.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `c` is the original number of digits in `a`, `a` is updated based on the digits of the original value, `b` is the input integer converted from a string, `ans` is the minimum of `a % b` encountered.
    print(ans)
#Overall this is what the function does:The function accepts a string representing a positive integer `a` (with a length between 2 and 200,000 digits) and an integer `b` (where 2 ≤ b ≤ 10^8). It calculates the minimum value of `a % b` after potentially rearranging the digits of `a` (by moving the last non-zero digit to the front) and considers various configurations of `a` while iterating through its digits. The final result, which is printed, is the minimum modulo value found. The function does not handle invalid inputs or leading zeros as per the constraints provided.

