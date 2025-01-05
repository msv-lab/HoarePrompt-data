#State of the program right berfore the function call: The input integer is a string representation of a positive integer with a length between 2 and 200,000 digits, and m is an integer such that 2 ≤ m ≤ 10^8.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `c` is greater than 0, `i` is equal to `c`, `a` is modified based on the digits of the original value of 'a', and `ans` is the minimum value of the modified 'a' modulo 'b' during the iterations.
    print(ans)
#Overall this is what the function does:The function accepts two integers as input, where the first integer is expected to be a positive number with potentially up to 200,000 digits, and the second is a positive integer between 2 and 10^8. It calculates the minimum value of the first integer modulo the second integer after performing a series of digit manipulations. Specifically, it rotates the digits of the first integer and checks the modulo for each rotation to find the minimum value. Finally, it prints this minimum value. The function does not return a value; it simply outputs the result.

