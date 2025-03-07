#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^3, `x` is an integer such that 1 ≤ x ≤ 10^8, `n` is an integer such that 1 ≤ n ≤ x, `ans` is the maximum value between any divisor `i` of `x` and `x//i` where `n` is less than or equal to either `i` or `x//i`.
    print(ans)
    #This is printed: ans (where ans is the maximum value between any divisor i of x and x//i such that n is less than or equal to either i or x//i)
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( x \), and \( n \). For each test case, it calculates the maximum value between any divisor \( i \) of \( x \) and \( x // i \) where \( n \) is less than or equal to either \( i \) or \( x // i \). The function then prints this maximum value for each test case.

