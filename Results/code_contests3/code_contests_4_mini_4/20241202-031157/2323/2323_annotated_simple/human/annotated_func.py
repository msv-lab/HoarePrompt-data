#State of the program right berfore the function call: Stepan's integer is a string of digits (length between 2 and 200,000), and m is an integer between 2 and 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `copya` is 0, `c` is the number of digits in the original value of 'a', and 'Stepan's integer' is a string of digits, `m` is an integer between 2 and 10^8.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `c` is the original number of digits in 'a', `ans` is the minimum value of `a % b` among all non-zero last digits of 'a', `a` is the original value of 'a' with its digits potentially rotated, and `i` is equal to `c`.
    print(ans)
#Overall this is what the function does:The function accepts two integer inputs, `a` and `b`, where `a` is expected to be a string of digits with a length between 2 and 200,000, and `b` is an integer between 2 and 10^8. It calculates the minimum value of `a % b` after potentially rotating the digits of `a` if the last digit is non-zero. The function outputs this minimum value. If all last digits are zero, it does not change the value of `a` and will only return the original `a % b`.

