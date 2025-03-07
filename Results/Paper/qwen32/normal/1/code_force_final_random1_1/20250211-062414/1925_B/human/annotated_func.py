#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³. For each test case, x and n are integers such that 1 ≤ x ≤ 10⁸ and 1 ≤ n ≤ x.
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
        
    #State: a sequence of t integers, each representing the largest divisor d of x for each test case that satisfies the given conditions.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `x` and `n`. For each test case, it calculates and prints the largest divisor `d` of `x` such that `(x - n * d)` is non-negative and divisible by `d`.

