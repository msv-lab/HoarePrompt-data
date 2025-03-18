#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each of the following t lines contains two integers n and k such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: a series of integers, each representing the result of the corresponding test case based on the given conditions.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers `n` and `k`. For each test case, it calculates and prints an integer result based on the specific conditions involving `n` and `k`. The result is determined by whether `k` is less than or equal to `4 * n - 4`, equal to `4 * n - 3`, or equal to `4 * n - 2`.

