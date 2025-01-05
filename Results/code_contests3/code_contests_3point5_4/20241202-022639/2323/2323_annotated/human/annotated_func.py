#State of the program right berfore the function call: Stepan's integer is a positive integer with a length between 2 and 200,000 digits, inclusive. The integer does not contain leading zeros. The number m is an integer such that 2 ≤ m ≤ 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: Stepan's integer is a positive integer with a length between 2 and 200,000 digits, `m` is an integer such that 2 ≤ m ≤ 10^8, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: After the loop executes, `a` will have undergone a transformation where its digits have been rearranged, `ans` will hold the minimum value of `a % b` after each iteration, `m` and `b` will remain unchanged, and `copya` will still be 0.
    print(ans)
#Overall this is what the function does:The function `func` reads two integers `a` and `b` as input. It calculates the number of digits in `a` and then performs a series of operations on `a` to find the minimum value of `a % b`. The final minimum value is printed as the output. The function does not accept any parameters explicitly, but it operates on the input values of `a` and `b` based on the described constraints.

