#State of the program right berfore the function call: Stepan's integer is a string representing a positive integer with a length between 2 and 200,000 digits, and m is an integer such that 2 ≤ m ≤ 10^8.
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: Stepan's integer is a string representing a positive integer with a length between 2 and 200,000 digits; `a` is an input integer; `b` is an input integer; `c` is the length of Stepan's integer; `copya` is 0.
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
        
    #State of the program after the  for loop has been executed: `copya` is 0, `ans` is the minimum value of `a % b` obtained from all valid iterations, `c` is the length of Stepan's integer, and `a` is a permutation of its original digits.
    print(ans)
#Overall this is what the function does:The function accepts two inputs: a positive integer represented as a string (Stepan's integer) and an integer m (where 2 ≤ m ≤ 10^8). It computes and prints the minimum value of the integer formed by permutations of the digits of Stepan's integer modulo m. The function considers all possible single-digit rotations of the number, ensuring that leading zeros are handled correctly. It does not return any value, as it directly prints the result instead.

