#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, x and n are integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
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
        
    #State: For each test case, `ans` is the largest divisor `d` of `x` such that `x - n * d` is non-negative and divisible by `d`.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `x` and `n`. For each test case, it finds the largest divisor `d` of `x` such that `x - n * d` is non-negative and divisible by `d`, and prints this divisor.

