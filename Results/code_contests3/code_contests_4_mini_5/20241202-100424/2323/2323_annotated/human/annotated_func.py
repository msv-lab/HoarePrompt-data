#State of the program right berfore the function call: the input consists of a string representing a positive integer with a length between 2 and 200,000 digits, and an integer m (2 ≤ m ≤ 10^8) which is the divisor for the good shifts of the integer.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `c` is the number of digits in the original value of `a`, `copya` is 0. If `a` is 0, then `c` is 0.
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
        
    #State of the program after the  for loop has been executed: `c` is the number of digits in the original value of `a`, `h` is the last digit of the original value of `a`, `a` is the transformed value after all iterations, `ans` is the minimum value of `a % b` encountered during the iterations.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `a` (given as a string) and an integer `b` (the divisor) and calculates the minimum value of `a % b` after performing "good shifts" on `a`. A good shift is performed by moving the last digit of `a` to the front, but if the last digit is `0`, it does not affect the value of `a`. The function prints the minimum result of `a % b` after all shifts, but it does not handle cases where the input value of `a` might be zero, as it assumes `a` is always a positive integer.

