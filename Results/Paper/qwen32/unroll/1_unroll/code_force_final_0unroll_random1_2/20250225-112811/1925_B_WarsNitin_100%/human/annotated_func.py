#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each of the t test cases, x and n are integers such that 1 <= x <= 10^8 and 1 <= n <= x.
def func():
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: a list of t integers, where each integer is the maximum valid divisor for the corresponding test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `x` and `n`. For each test case, it calculates and prints the maximum divisor of `x` such that subtracting `n` times the divisor from `x` results in a non-negative number that is also divisible by the divisor.

